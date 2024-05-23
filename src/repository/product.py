from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.product import ProductCreate, ProductUpdate
from src.models.product import ProductModel

class ProductRepository():
    def __init__(self, db: Session):
        self.db = db

    def list(self, skip: int, limit: int):
        return self.db.query(ProductModel).offset(skip).limit(limit).all()

    def get(self, id: str):
        product = self.db.query(ProductModel).filter(ProductModel.id == id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Not found")
        
        return product

    def create(self, user_id: str, product: ProductCreate):
        new_product = ProductModel(**product.model_dump(), user_id=user_id)

        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product
    
    def update(self, id: str, user_id: str, product: ProductUpdate):
        stored_product = self.get(id)

        if stored_product.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to update this resource")

        for field in product.model_dump(exclude_unset=True):
            setattr(stored_product, field, getattr(product, field))

        self.db.commit()
        self.db.refresh(stored_product)
        return stored_product

    def delete(self, id: str, user_id: str):
        stored_product = self.get(id)
        
        if stored_product.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to delete this resource")
    
        self.db.delete(stored_product)
        self.db.commit()
        return {"detail": "Resource deleted successfully"}