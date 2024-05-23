from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from src.config.database import get_db
from src.schemes.user import UserList
from src.schemes.profile import Profile
from src.repository.user import UserRepository

router = APIRouter()
db: Session = next(get_db())

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[UserList])
async def list(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return UserRepository(db).list(skip=skip, limit=limit)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Profile)
async def get(id: str, db: Session = Depends(get_db)):
    return UserRepository(db).get(id)