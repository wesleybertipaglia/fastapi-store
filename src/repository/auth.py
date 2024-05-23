from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from src.schemes.auth import SignIN, SignUP
from src.models.user import UserModel
from src.repository.user import UserRepository
from src.providers.hash import Hash
from src.providers.token import Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthRepository():
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def sign_in(self, user: SignIN):
        stored_user = self.user_repository.get_by_email(user.email)
        
        if not stored_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        if not Hash.verify(stored_user.password, user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")
        
        token = Token().create_access_token(data={"sub": stored_user.email})
        return {"access_token": token, "token_type": "bearer"}
    
    def sign_up(self, user: SignUP):
        return UserRepository(self.db).create(user)
    
    def sign_out(self, token: str = Depends(oauth2_scheme)):
        token = Token().revoke_access_token(token)
        return {"access_token": token, "token_type": "bearer", "detail": "Token revoked"}     
        
    def get_current_user(self, token: str = Depends(oauth2_scheme)):
        email = Token().verify_token(token)
        user_data: UserModel = self.user_repository.get_by_email(email)
        
        if not user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

        return user_data
    
    def get_current_user_id(self, token: str = Depends(oauth2_scheme)):
        user = self.get_current_user(token)
        return user.id