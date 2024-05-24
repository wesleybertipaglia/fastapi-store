from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.order import Order, OrderCreate, OrderUpdate, OrderItem, OrderSingle, OrderPayment, OrderShipping
from src.models.order import OrderModel, OrderItemsModel, OrderPaymentModel, OrderShippingModel
from src.repository.product import ProductRepository

class OrderRepository():
    def __init__(self, db: Session):
        self.db = db    
    
    def list(self, user_id: str, skip: int, limit: int):
        try:
            return self.db.query(OrderModel).filter(OrderModel.user_id == user_id).offset(skip).limit(limit).all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while fetching your request: {e}")
        
    def get(self, id: str, user_id: str):
        stored_order = self.db.query(OrderModel).filter(OrderModel.id == id).first()
        
        if not stored_order:
            raise HTTPException(status_code=404, detail="Not found")
        if stored_order.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to view this resource")
        
        payment = self.db.query(OrderPaymentModel).filter(OrderPaymentModel.order_id == id).first()
        shipping = self.db.query(OrderShippingModel).filter(OrderShippingModel.order_id == id).first()

        if payment:
            payment = OrderPayment(**payment.__dict__)        

        if shipping:
            shipping = OrderShipping(**shipping.__dict__)
        
        stored_order_items = self.db.query(OrderItemsModel).filter(OrderItemsModel.order_id == id).all()
        order_items = [OrderItem(**item.__dict__) for item in stored_order_items]        
        return OrderSingle(**stored_order.__dict__, items=order_items, payment=payment, shipping=shipping)
    
    def create(self, user_id: str, order: OrderCreate):
        total, total_products = 0, 0
        
        new_order = OrderModel(
            user_id=user_id,
            status=order.status,
            total_products=0,
            total=0.0
        )
        
        if new_order:
            self.db.add(new_order)
            self.db.flush()
        else:
            raise HTTPException(status_code=400, detail="An error occurred while creating the order")

        if order.shipping:
            new_shipping = OrderShippingModel(**order.shipping.model_dump(), order_id=new_order.id)
            self.db.add(new_shipping)
        
        if order.payment:
            new_payment = OrderPaymentModel(**order.payment.model_dump(), order_id=new_order.id)
            self.db.add(new_payment)

        for item in order.items:
            stored_product =  ProductRepository(self.db).get(item.product_id)

            if stored_product.stock < item.quantity:
                raise HTTPException(status_code=400, detail="One or more products are out of stock.")

            stored_product.stock -= item.quantity
            self.db.refresh(stored_product)

            new_order_item = OrderItemsModel(**item.model_dump(exclude_unset=True), order_id=new_order.id, total=item.quantity * stored_product.price)
            self.db.add(new_order_item)

            total += new_order_item.total
            total_products += new_order_item.quantity            
        
        new_order.total = total
        new_order.total_products = total_products
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def update(self, id: str, user_id: str, order: OrderUpdate):
        stored_order = self.get(id=id, user_id=user_id)        

        if not stored_order:
            raise HTTPException(status_code=404, detail="Not found")
        if stored_order.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to update this resource")   
        
        stored_order_items = self.db.query(OrderItemsModel).filter(OrderItemsModel.order_id == id).all()
        for item in stored_order_items:
            for field in item.model_dump(exclude_unset=True):
                setattr(item, field, getattr(order, field))                        
            
        for field in order.model_dump(exclude_unset=True):
            setattr(stored_order, field, getattr(order, field))        

        self.db.commit()
        self.db.refresh(stored_order)
        return stored_order

    def delete(self, id: str, user_id: str):
        stored_order = self.get(id=id, user_id=user_id)

        if stored_order.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to delete this resource")

        self.db.delete(stored_order)
        self.db.commit()
        return {"detail": "Resource deleted successfully"}