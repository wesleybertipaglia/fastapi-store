from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.order import Order, OrderCreate, OrderUpdate
from src.repository.order import OrderRepository
from src.repository.auth import AuthRepository
from typing import List

router = APIRouter()
db: Session = next(get_db())

@router.get('/', response_model=List[Order])
def list_orders(db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return OrderRepository(db).list_orders(current_user_id)

@router.get('/{id}', response_model=Order)
def get_order(id: str, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return OrderRepository(db).get_order(id=id, user_id=current_user_id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return OrderRepository(db).create_order(user_id=current_user_id, order=order)

@router.put('/{id}', response_model=Order)
def update_order(id: str, order: OrderUpdate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return OrderRepository(db).update_order(id=id, user_id=current_user_id, order=order)

@router.delete('/{id}')
def delete_order(id: str, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return OrderRepository(db).delete_order(id=id, user_id=current_user_id)