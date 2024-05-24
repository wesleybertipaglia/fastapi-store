from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.order import OrderItem, OrderSingle
from src.repository.auth import AuthRepository
from src.repository.sales import SalesRepository

router = APIRouter()
db: Session = next(get_db())

@router.get('/', response_model=list[OrderItem])
async def list(current_user_id: str = Depends(AuthRepository(db).get_current_user_id), skip: int = 0, limit: int = 0):
    return SalesRepository(db).list(user_id=current_user_id, skip=skip, limit=limit)

@router.get('/{id}', response_model=OrderItem)
async def get(id: str, current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return SalesRepository(db).get(id=id, user_id=current_user_id)