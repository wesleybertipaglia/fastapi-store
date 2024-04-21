from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.product import Product, ProductResponse, ProductUpdate
from src.repository.product import ProductRepository
from typing import List

router = APIRouter()

# rules
    # the list of public information of all products can be accessed by anyone
    # a public information of a product can be accessed by anyone
    # a product only can be created if the user is authenticated
    # the product only can be updated or deleted by the user itself
    # private information of a product can be accessed only by the user itself

# improvements
    # change id to uuid
    # implement stock
    # implement category
    # implement tags
    # implement images
    # implement reviews and rating

# auth
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
def create_product(product: Product, db: Session = Depends(get_db)):
    return ProductRepository(db).create(product)

# only open information
@router.get('/', response_model=List[Product])
def list_products(db: Session = Depends(get_db)):
    return ProductRepository(db).list()

# only open information
@router.get('/{id}')
def get_product(id: str, db: Session = Depends(get_db)):
    return ProductRepository(db).get(id)

# auth
@router.put('/{id}', response_model=ProductResponse)
def update_product(id: int,product: ProductUpdate, db: Session = Depends(get_db)):
    return ProductRepository(db).update(id, product)

# auth
@router.delete('/{id}')
def delete_product(id: str, db: Session = Depends(get_db)):
    return ProductRepository(db).delete(id)