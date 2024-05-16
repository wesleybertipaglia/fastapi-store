from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.product import Product, ProductUpdate, ProductPublic, ProductPrivate
from src.repository.product import ProductRepository
from src.repository.auth import AuthRepository
from typing import List

router = APIRouter()
db: Session = next(get_db())

@router.get('/', response_model=List[ProductPublic])
def list_products(db: Session = Depends(get_db)):
    return ProductRepository(db).list_products()

@router.get('/{id}', response_model=ProductPublic)
def get_product(id: str, db: Session = Depends(get_db)):
    return ProductRepository(db).get_product(id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProductPrivate)
def create_product(product: Product, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return ProductRepository(db).create_product(user_id=current_user_id, product=product)

@router.put('/{id}', response_model=ProductPrivate)
def update_product(id: str, product: ProductUpdate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return ProductRepository(db).update_product(id=id, user_id=current_user_id, product=product)

@router.delete('/{id}')
def delete_product(id: str, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return ProductRepository(db).delete_product(id=id, user_id=current_user_id)