from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from src.config.database import get_db
from src.schemes.user import UserPublic
from src.schemes.profile import Profile
from src.repository.user import UserRepository
from src.schemes.product import ProductPublic

router = APIRouter()
db: Session = next(get_db())

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[UserPublic])
async def list_users(db: Session = Depends(get_db)):
    return UserRepository(db).list_users()

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Profile)
async def get_user(id: str, db: Session = Depends(get_db)):
    return UserRepository(db).get_user(id)