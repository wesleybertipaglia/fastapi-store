from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.profile import ProfileSingle, ProfileUpdate
from src.repository.auth import AuthRepository
from src.repository.user import UserRepository

router = APIRouter()
db: Session = next(get_db())

@router.get('/', status_code=status.HTTP_200_OK, response_model=ProfileSingle)
async def profile(current_user: ProfileSingle = Depends(AuthRepository(db).get_current_user)):
    return current_user

@router.put('/update', response_model=ProfileSingle)
async def update(updated_user: ProfileUpdate, current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return UserRepository(db).update(id=current_user_id, user=updated_user)