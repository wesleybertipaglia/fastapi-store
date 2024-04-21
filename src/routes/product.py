from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.product import Product, ProductResponse, ProductUpdate
from src.repository.product import ProductRepository
from typing import List

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
def create_product(product: Product, db: Session = Depends(get_db)):
    return ProductRepository(db).create(product)

@router.get('/', response_model=List[Product])
def list_products(db: Session = Depends(get_db)):
    return ProductRepository(db).list()

@router.get('/{id}')
def get_product(id: str, db: Session = Depends(get_db)):
    return ProductRepository(db).get(id)

@router.put('/{id}', response_model=ProductResponse)
def update_product(id: int,product: ProductUpdate, db: Session = Depends(get_db)):
    return ProductRepository(db).update(id, product)

@router.delete('/{id}')
def delete_product(id: str, db: Session = Depends(get_db)):
    return ProductRepository(db).delete(id)