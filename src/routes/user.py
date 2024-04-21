from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.user import UserPublic
from src.repository.user import UserRepository
from src.schemes.product import ProductPublic
from typing import List

router = APIRouter()
db: Session = next(get_db())

# improvements
    # change id to uuid
    # implement roles
    # implement permissions
    # implement profile information (avatar, username, bio)
    # implement address information
    # implement contact information
    # implement payment information

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[UserPublic])
async def list_users(db: Session = Depends(get_db)):
    return UserRepository(db).list_users()

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=UserPublic)
async def get_user(id: str, db: Session = Depends(get_db)):
    return UserRepository(db).get_user(id)

@router.get('/{id}/products', status_code=status.HTTP_200_OK, response_model=List[ProductPublic])
async def get_user_products(id: str, db: Session = Depends(get_db)):
    return UserRepository(db).get_products(id)