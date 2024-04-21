from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.order import Order, OrderResponse, OrderUpdate
from src.repository.order import OrderRepository
from typing import List

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=OrderResponse)
def create_order(order: Order, db: Session = Depends(get_db)):
    return OrderRepository(db).create(order)

@router.get('/', response_model=List[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return OrderRepository(db).list()

@router.get('/{id}', response_model=OrderResponse)
def get_order(id: str, db: Session = Depends(get_db)):
    return OrderRepository(db).get(id)

@router.put('/{id}', response_model=OrderResponse)
def update_order(id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    return OrderRepository(db).update(id, order)

@router.delete('/{id}')
def delete_order(id: str, db: Session = Depends(get_db)):
    return OrderRepository(db).delete(id)