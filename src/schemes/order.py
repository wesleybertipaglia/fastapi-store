from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id: Optional[str] = None
    user_id: str
    payment_id: str
    shipping_id: str
    status: str
    total_products: Optional[int] = 0
    tax: Optional[float] = 0.0
    total: Optional[float] = None
    items: Optional[list] = None

    class Config:
        from_attributes = True

class OrderItem(BaseModel):
    id: Optional[str] = None
    order_id: Optional[str] = None
    product_id: Optional[str] = None
    seller_id: Optional[str] = None
    quantity: Optional[int] = 1
    total: Optional[float] = None

    class Config:
        from_attributes = True

class OrderPayment(BaseModel):
    id: Optional[str] = None
    payment_method_id: str
    status: Optional[str] = "pending"

    class Config:
        from_attributes = True

class OrderShipping(BaseModel):
    id: Optional[str] = None
    address_id: Optional[str] = None
    tracking_number: Optional[str] = None
    status: Optional[str] = "pending"
    note: Optional[str] = None

    class Config:
        from_attributes = True

class OrderList(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    status: Optional[str] = None
    total: Optional[float] = None

    class Config:
        from_attributes = True

class OrderSingle(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = None
    total_products: Optional[int] = 0
    tax: Optional[float] = 0.0
    total: Optional[float] = None
    items: Optional[list] = None
    payment: Optional[OrderPayment] = None
    shipping: Optional[OrderShipping] = None

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = "processing"
    items: list[OrderItem]
    shipping: Optional[OrderShipping] = None
    payment: Optional[OrderPayment] = None

    class Config:
        from_attributes = True

class OrderUpdate(BaseModel):
    status: str
    total_products: int    
    tax: Optional[float] = 0.0
    total: Optional[float] = None
    items: Optional[list] = None
    payment_id: Optional[str] = None
    shipping_id: Optional[str] = None

    class Config:
        from_attributes = True