from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.auth import SignUP, SignIN, Delete
from src.schemes.user import UserPrivate
from src.repository.auth import AuthRepository
from src.repository.user import UserRepository

router = APIRouter()
db: Session = next(get_db())

@router.post('/up', status_code=status.HTTP_201_CREATED, response_model=UserPrivate)
async def sign_up(user: SignUP):
    return AuthRepository(db).sign_up(user)

@router.post('/in')
async def sign_in(user: SignIN):
    return AuthRepository(db).sign_in(user)

@router.post('/out')
async def sign_out(token: str = Depends(AuthRepository(db).sign_out)):
    return AuthRepository(db).sign_out(token)

@router.delete('/delete')
async def delete(user: Delete, current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return UserRepository(db).delete_user(current_user_id, user.password)