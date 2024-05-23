from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.address import AddressCreate, AddressUpdate
from src.models.address import AddressModel

class AddressRepository():
    def __init__(self, db: Session):
        self.db = db

    def list(self, user_id: str, skip: int, limit: int):
        try:
            return self.db.query(AddressModel).filter(AddressModel.user_id == user_id).offset(skip).limit(limit).all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while fetching your request: {e}.")

    def get(self, id: str):
        address = self.db.query(AddressModel).filter(AddressModel.id == id).first()

        if not address:
            raise HTTPException(status_code=404, detail="Not found")
        
        return address

    def create(self, user_id: str, address: AddressCreate):
        new_address = AddressModel(**address.model_dump(exclude_unset=True), user_id=user_id)

        self.db.add(new_address)
        self.db.commit()
        self.db.refresh(new_address)
        return new_address
    
    def update(self, id: str, user_id: str, address: AddressUpdate):
        stored_address = self.get(id)

        if stored_address.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to update this resource")

        for field in address.model_dump(exclude_unset=True):
            setattr(stored_address, field, getattr(address, field))

        self.db.commit()
        self.db.refresh(stored_address)
        return stored_address

    def delete(self, id: str, user_id: str):
        stored_address = self.get(id)
        
        if stored_address.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to delete this resource")
    
        self.db.delete(stored_address)
        self.db.commit()
        return {"detail": "Resource deleted successfully"}