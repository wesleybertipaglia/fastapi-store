from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.payment import PaymentMethodSingle, PaymentMethodList, PaymentMethodCreate, PaymentMethodUpdate
from src.repository.payment import PaymentMethodRepository
from src.repository.auth import AuthRepository
from typing import List

router = APIRouter()
db: Session = next(get_db())

@router.get('/', response_model=List[PaymentMethodList])
def list(db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id), skip: int = 0, limit: int = 10):
    return PaymentMethodRepository(db).list(user_id=current_user_id, skip=skip, limit=limit)

@router.get('/{id}', response_model=PaymentMethodSingle)
def get(id: str, db: Session = Depends(get_db)):
    return PaymentMethodRepository(db).get(id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PaymentMethodSingle)
def create(payment_method: PaymentMethodCreate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return PaymentMethodRepository(db).create(user_id=current_user_id, payment_method=payment_method)

@router.put('/{id}', response_model=PaymentMethodSingle)
def update(id: str, payment_method: PaymentMethodUpdate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return PaymentMethodRepository(db).update(id=id, user_id=current_user_id, payment_method=payment_method)

@router.delete('/{id}')
def delete(id: str, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return PaymentMethodRepository(db).delete(id=id, user_id=current_user_id)