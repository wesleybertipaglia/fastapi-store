from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.auth import SignIN, SignUP
from src.models.user import UserModel
from src.providers.hash import Hash

class AuthRepository():
    def __init__(self, db: Session):
        self.db = db

    def sign_in(self, user: SignIN):
        stored_user = self.get_by_email(user.email)
        if not stored_user:
            raise HTTPException(status_code=404, detail="User not found")
        if not Hash.verify(stored_user.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid password")
        return stored_user
    
    def sign_up(self, user: SignUP):
        if self.get_by_email(user.email):
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
    
    def get_by_email(self, email):
        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        return user