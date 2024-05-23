from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.product import ProductSingle, ProductList, ProductCreate, ProductUpdate
from src.repository.product import ProductRepository
from src.repository.auth import AuthRepository
from typing import List

router = APIRouter()
db: Session = next(get_db())

@router.get('/', response_model=List[ProductList])
def list(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return ProductRepository(db).list(skip=skip, limit=limit)

@router.get('/{id}', response_model=ProductSingle)
def get(id: str, db: Session = Depends(get_db)):
    return ProductRepository(db).get(id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProductSingle)
def create(product: ProductCreate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return ProductRepository(db).create(user_id=current_user_id, product=product)

@router.put('/{id}', response_model=ProductSingle)
def update(id: str, product: ProductUpdate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return ProductRepository(db).update(id=id, user_id=current_user_id, product=product)

@router.delete('/{id}')
def delete(id: str, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return ProductRepository(db).delete(id=id, user_id=current_user_id)