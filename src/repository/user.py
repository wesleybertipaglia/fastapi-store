from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.user import User, UserUpdate
from src.models.user import UserModel
from src.models.product import ProductModel
from src.providers.hash import Hash

class UserRepository():
    def __init__(self, db: Session):
        self.db = db
    
    def list_users(self):
        return self.db.query(UserModel).all()

    def get_user(self, id: str):
        stored_user = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not stored_user:
            raise HTTPException(status_code=404, detail="User not found")
        return stored_user
    
    def get_user_by_email(self, email: str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def get_user_products(self, id: str):
        return self.db.query(ProductModel).filter(ProductModel.user_id == id).all()

    def create_user(self, user: User):
        if self.get_user_by_email(user.email):
            raise HTTPException(status_code=400, detail="Email already registered")

        new_user = UserModel(
            name=user.name,
            email=user.email,
            password=Hash.bcrypt(user.password)
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def update_user(self, id: str, user: UserUpdate):
        stored_user = self.get_user(id)

        if user.email != stored_user.email:
            if self.get_user_by_email(user.email):
                raise HTTPException(status_code=400, detail="Email already registered")
            
        if user.password:
            user.password = Hash.bcrypt(user.password)

        for field in user.model_dump(exclude_unset=True):
            setattr(stored_user, field, getattr(user, field))

        self.db.commit()
        self.db.refresh(stored_user)
        return stored_user

    def delete_user(self, id: str):        
        stored_user = self.get_user(id)
        self.db.delete(stored_user)
        self.db.commit()
        return {"detail": "User deleted"}    