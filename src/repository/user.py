from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.schemes.user import UserUpdate
from src.schemes.auth import SignUP
from src.models.user import UserModel
from src.providers.hash import Hash

class UserRepository():
    def __init__(self, db: Session):
        self.db = db
    
    def list(self, skip: int, limit: int):
        return self.db.query(UserModel).offset(skip).limit(limit).all()

    def get(self, id: str):
        stored_user = self.db.query(UserModel).filter(UserModel.id == id).first()
        
        if not stored_user:
            raise HTTPException(status_code=404, detail="Not found")
        
        return stored_user
    
    def get_by_email(self, email: str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def get_by_username(self, username: str):
        return self.db.query(UserModel).filter(UserModel.username == username).first()

    def create(self, user: SignUP):
        if self.get_by_username(user.username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
        
        if self.get_by_email(user.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        try:
            new_user = UserModel(**user.model_dump(exclude_unset=True, exclude={"password"}), password=Hash.bcrypt(user.password))
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")
        finally:
            self.db.close()
    
    def update(self, id: str, user: UserUpdate):
        stored_user = self.get(id)

        if user.email and user.email != stored_user.email:
            if self.get_by_email(user.email):
                raise HTTPException(status_code=400, detail="Email already registered")
            
        if user.username and user.username != stored_user.username:
            if self.get_by_username(user.username):
                raise HTTPException(status_code=400, detail="Username already registered")
            
        if user.password:
            user.password = Hash.bcrypt(user.password)

        for field in user.model_dump(exclude_unset=True):
            setattr(stored_user, field, getattr(user, field))

        self.db.commit()
        self.db.refresh(stored_user)
        return stored_user

    def delete(self, id: str, password: str):        
        stored_user = self.get(id)
        
        if not Hash.verify(stored_user.password, password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")
        
        self.db.delete(stored_user)
        self.db.commit()
        return {"detail": "Resource deleted successfully"}