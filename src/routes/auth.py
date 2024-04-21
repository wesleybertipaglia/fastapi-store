from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.auth import SignUP, SignIN, UserResponse
from src.repository.auth import AuthRepository

router = APIRouter()
db: Session = next(get_db())

@router.post('/up', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def sign_up(user: SignUP):
    return AuthRepository(db).sign_up(user)

@router.post('/in')
async def sign_in(user: SignIN):
    return AuthRepository(db).sign_in(user)

@router.post('/out')
async def sign_out(token: str = Depends(AuthRepository(db).sign_out)):
    return AuthRepository(db).sign_out(token)