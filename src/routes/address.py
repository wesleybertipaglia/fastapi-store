from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemes.address import AddressList, AddressSingle, AddressCreate, AddressUpdate
from src.repository.address import AddressRepository
from src.repository.auth import AuthRepository
from typing import List

router = APIRouter()
db: Session = next(get_db())

@router.get('/', response_model=List[AddressList])
def list(db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id), skip: int = 0, limit: int = 10):
    return AddressRepository(db).list(user_id=current_user_id, skip=skip, limit=limit)

@router.get('/{id}', response_model=AddressSingle)
def get(id: str, db: Session = Depends(get_db)):
    return AddressRepository(db).get(id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=AddressSingle)
def create(address: AddressCreate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return AddressRepository(db).create(user_id=current_user_id, address=address)

@router.put('/{id}', response_model=AddressSingle)
def update(id: str, address: AddressUpdate, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return AddressRepository(db).update(id=id, user_id=current_user_id, address=address)

@router.delete('/{id}')
def delete(id: str, db: Session = Depends(get_db), current_user_id: str = Depends(AuthRepository(db).get_current_user_id)):
    return AddressRepository(db).delete(id=id, user_id=current_user_id)