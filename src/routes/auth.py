from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.auth import SignUP, SignIN
from src.repository.auth import AuthRepository

router = APIRouter()
db: Session = next(get_db())

@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def sign_up(user: SignUP):
    return AuthRepository(db).sign_up(user)

@router.post('/signin')
async def sign_in(user: SignIN):
    return AuthRepository(db).sign_in(user)

@router.get('/me')
async def me(current_user = Depends(AuthRepository(db).get_logged_user)):
    return current_user