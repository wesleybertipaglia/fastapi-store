from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.user import User, UserResponse, UserUpdate
from src.repository.user import UserRepository
from typing import List

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: User, db: Session = Depends(get_db)):
    return UserRepository(db).create(user)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[User])
async def list_users(db: Session = Depends(get_db)):
    return UserRepository(db).list()

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_user(id: str, db: Session = Depends(get_db)):
    return UserRepository(db).get(id)

@router.put('/{id}', response_model=UserResponse)
async def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return UserRepository(db).update(id, user)

@router.delete('/{id}')
async def delete_user(id: str, db: Session = Depends(get_db)):
    return UserRepository(db).delete(id)
