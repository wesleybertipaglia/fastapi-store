from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.product import Product, ProductUpdate
from src.models.product import ProductModel

class ProductRepository():
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: Product):
        new_product = ProductModel(
            name=product.name,
            description=product.description,
            price=product.price,
            available=product.available,
            user_id=product.user_id
        )

        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def list(self):
        return self.db.query(ProductModel).all()

    def get(self, id):
        product = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product    

    def update(self, id: int, product: ProductUpdate):
        stored_product = self.get(id)

        for field in product.model_dump(exclude_unset=True):
            setattr(stored_product, field, getattr(product, field))

        self.db.commit()
        self.db.refresh(stored_product)
        return stored_product

    def delete(self, id):
        product = self.get(id)
        self.db.delete(product)
        self.db.commit()
        return {"detail": "Product deleted"}