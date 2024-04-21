from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.auth import SignUP, SignIN, UserResponse
from src.repository.auth import AuthRepository
from typing import List

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def sign_up(user: SignUP, db: Session = Depends(get_db)):
    return AuthRepository(db).sign_up(user)

@router.post('/signin', response_model=UserResponse)
async def sign_in(user: SignIN, db: Session = Depends(get_db)):
    return AuthRepository(db).sign_in(user)