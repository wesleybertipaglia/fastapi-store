from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.user import UserUpdate, UserPrivate
from src.repository.auth import AuthRepository
from src.repository.user import UserRepository

router = APIRouter()
db: Session = next(get_db())

@router.get('/', status_code=status.HTTP_200_OK, response_model=UserPrivate)
async def profile(current_user: UserPrivate = Depends(AuthRepository(db).get_current_user)):
    return current_user

@router.put('/update', response_model=UserPrivate)
async def update(updated_user: UserUpdate, current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return UserRepository(db).update_user(id=current_user_id, user=updated_user)

@router.delete('/delete')
async def delete(current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return UserRepository(db).delete_user(current_user_id)