from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.product import Product, ProductUpdate
from src.models.product import ProductModel

class ProductRepository():
    def __init__(self, db: Session):
        self.db = db

    def list_products(self):
        return self.db.query(ProductModel).all()

    def get_product(self, id: str):
        product = self.db.query(ProductModel).filter(ProductModel.id == id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        return product

    def create_product(self, user_id: str, product: Product):
        new_product = ProductModel(
            name=product.name,
            description=product.description,
            price=product.price,
            available=product.available,
            user_id=user_id
        )

        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product
    
    def update_product(self, id: str, user_id: str, product: ProductUpdate):
        stored_product = self.get_product(id)

        if stored_product.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to update this product")

        for field in product.model_dump(exclude_unset=True):
            setattr(stored_product, field, getattr(product, field))

        self.db.commit()
        self.db.refresh(stored_product)
        return stored_product

    def delete_product(self, id: str, user_id: str):
        stored_product = self.get_product(id)
        
        if stored_product.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to update this product")
    
        self.db.delete(stored_product)
        self.db.commit()
        return {"detail": "Product deleted"}