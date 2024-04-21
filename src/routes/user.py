from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.user import User, UserResponse, UserUpdate
from src.repository.user import UserRepository
from typing import List

router = APIRouter()

# rules
    # the list of public information of all users can be accessed by anyone
    # a public information of a user can be accessed by anyone
    # a user only can be created if the user is not authenticated
    # the user only can be updated or deleted by the user itself
    # private information of a user can be accessed only by the user itself

# improvements
    # change id to uuid
    # implement roles
    # implement permissions
    # implement profile information (avatar, username, bio)
    # implement address information
    # implement contact information
    # implement payment information

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: User, db: Session = Depends(get_db)):
    return UserRepository(db).create(user)

# only open information
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[User])
async def list_users(db: Session = Depends(get_db)):
    return UserRepository(db).list()

# only open information
@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_user(id: str, db: Session = Depends(get_db)):
    return UserRepository(db).get(id)

# auth
@router.put('/{id}', response_model=UserResponse)
async def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return UserRepository(db).update(id, user)

# auth
@router.delete('/{id}')
async def delete_user(id: str, db: Session = Depends(get_db)):
    return UserRepository(db).delete(id)
