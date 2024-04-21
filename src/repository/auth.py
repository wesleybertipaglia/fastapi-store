from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from src.schemes.auth import SignIN, SignUP, UserResponse
from src.models.user import UserModel
from src.providers.hash import Hash
from src.providers.token import Token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthRepository():
    def __init__(self, db: Session):
        self.db = db

    def sign_in(self, user: SignIN):
        stored_user = self.get_by_email(user.email)
        if not stored_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        if not Hash.verify(stored_user.password, user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")
        
        token = Token().create_access_token(data={"sub": stored_user.email})
        return {"access_token": token, "token_type": "bearer"}
    
    def sign_up(self, user: SignUP):
        if self.get_by_email(user.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        new_user = UserModel(
            name=user.name,
            email=user.email,
            password=Hash.bcrypt(user.password)
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        
        token = Token().create_access_token(data={"sub": new_user.email})
        return {"access_token": token, "token_type": "bearer"}
    
    def get_by_email(self, email):
        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        return user
    
    def get_logged_user(self, token: str = Depends(oauth2_scheme)):
        email = Token().verify_token(token)
        user_data: UserResponse = self.get_by_email(email)
        user = UserResponse(**user_data.__dict__)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user