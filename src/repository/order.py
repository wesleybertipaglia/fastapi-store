from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.order import Order, OrderUpdate
from src.models.order import OrderModel
from src.repository.product import ProductRepository

class OrderRepository():
    def __init__(self, db: Session):
        self.db = db

    def create(self, order: Order):
        stored_product = ProductRepository(self.db).get(order.product_id)
        
        new_order = OrderModel(
            user_id=order.user_id,
            product_id=order.product_id,
            quantity=order.quantity,
            total=order.quantity * stored_product.price
        )

        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def list(self):
        return self.db.query(OrderModel).all()

    def get(self, id):
        order = self.db.query(OrderModel).filter(OrderModel.id == id).first()        
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

    def update(self, id:int, order: OrderUpdate):
        stored_order = self.get(id)

        for field in order.model_dump(exclude_unset=True):
            setattr(stored_order, field, getattr(order, field))

        self.db.commit()
        self.db.refresh(stored_order)
        return stored_order

    def delete(self, id):
        order = self.get(id)
        self.db.delete(order)
        self.db.commit()
        return {"detail": "Order deleted"}