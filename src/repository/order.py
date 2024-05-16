from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.order import OrderCreate, OrderUpdate
from src.models.order import OrderModel
from src.repository.product import ProductRepository

class OrderRepository():
    def __init__(self, db: Session):
        self.db = db

    def list_orders(self, user_id: str):
        return self.db.query(OrderModel).filter(OrderModel.user_id == user_id).all()

    def get_order(self, id: str, user_id: str):
        stored_order = self.db.query(OrderModel).filter(OrderModel.id == id).first()

        if not stored_order:
            raise HTTPException(status_code=404, detail="Order not found")
        if stored_order.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to update this order")                    
        
        return stored_order
    
    def create_order(self, user_id: str, order: OrderCreate):
        stored_product = self._get_product(order.product_id)
        
        new_order = OrderModel(
            user_id=user_id,
            product_id=order.product_id,
            quantity=order.quantity,
            total=order.quantity * stored_product.price
        )

        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def update_order(self, id: str, user_id: str, order: OrderUpdate):
        stored_order = self.get_order(id=id, user_id=user_id)
        stored_product = self._get_product(stored_order.product_id)
        stored_order.total = order.quantity * stored_product.price

        for field in order.model_dump(exclude_unset=True):
            setattr(stored_order, field, getattr(order, field))        

        self.db.commit()
        self.db.refresh(stored_order)
        return stored_order

    def delete_order(self, id: str, user_id: str):
        stored_order = self.get_order(id=id, user_id=user_id)

        self.db.delete(stored_order)
        self.db.commit()
        return {"detail": "Order deleted"}
    
    def _get_product(self, product_id: str):
        product = ProductRepository(self.db).get(product_id)
        return product