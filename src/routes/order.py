from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.order import OrderSingle, OrderList, OrderCreate, OrderUpdate
from src.repository.order import OrderRepository
from src.repository.auth import AuthRepository
from typing import List

router = APIRouter()
db: Session = next(get_db())

@router.get('/', response_model=List[OrderList])
def list(db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id), skip: int = 0, limit: int = 10):
    return OrderRepository(db).list(user_id=current_user_id, skip=skip, limit=limit)

@router.get('/{id}', response_model=OrderSingle)
def get(id: str, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return OrderRepository(db).get(id=id, user_id=current_user_id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=OrderSingle)
def create(order: OrderCreate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return OrderRepository(db).create(user_id=current_user_id, order=order)

@router.put('/{id}', response_model=OrderSingle)
def update(id: str, order: OrderUpdate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return OrderRepository(db).update(id=id, user_id=current_user_id, order=order)

@router.delete('/{id}')
def delete(id: str, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return OrderRepository(db).delete(id=id, user_id=current_user_id)