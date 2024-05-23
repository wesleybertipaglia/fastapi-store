from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.order import Order, OrderCreate, OrderUpdate, OrderItem
from src.models.order import OrderModel, OrderItemsModel, OrderPaymentModel
from src.models.payment import PaymentMethodModel
from src.repository.product import ProductRepository

class OrderRepository():
    def __init__(self, db: Session):
        self.db = db    
    
    def list_orders(self, user_id: str, skip: int, limit: int):
        try:
            return self.db.query(OrderModel).filter(OrderModel.user_id == user_id).offset(skip).limit(limit).all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while fetching orders: {e}.")

    def get_order(self, id: str, user_id: str):
        stored_order = self.db.query(OrderModel).filter(OrderModel.id == id).first()
        
        if not stored_order:
            raise HTTPException(status_code=404, detail="Order not found")
        if stored_order.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to update this order")
        
        stored_order_items = self.db.query(OrderItemsModel).filter(OrderItemsModel.order_id == id).all()
        order_items = [OrderItem(**item.__dict__) for item in stored_order_items]
        order = Order(**stored_order.__dict__)
        order.items = order_items
        
        return order
    
    def create_order(self, user_id: str, order: OrderCreate):
        total = 0
        total_products = 0
        
        new_order = OrderModel(
            user_id=user_id,
            status=order.status,
            total_products=0,
            tax=0.0,
            total=0
        )
        self.db.add(new_order)
        self.db.flush()

        new_payment = OrderPaymentModel(
            order_id=new_order.id,
            payment_method_id=order.payment_method_id,
            status=order.payment_status
        )
        self.db.add(new_payment)

        for item in order.items:
            stored_product =  ProductRepository(self.db).get_product(item.product_id)
            
            new_order_item = OrderItemsModel(
                order_id=new_order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                total=item.quantity * stored_product.price
            )

            total += new_order_item.total
            total_products += new_order_item.quantity
            self.db.add(new_order_item)
        
        new_order.total = total
        new_order.total_products = total_products
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def update_order(self, id: str, user_id: str, order: OrderUpdate):
        stored_order = self.get_order(id=id, user_id=user_id)
        stored_product = ProductRepository(self.db).get_product(stored_order.product_id)
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