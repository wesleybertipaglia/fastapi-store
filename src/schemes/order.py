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
    order_id: str
    product_id: str
    seller_id: str
    quantity: Optional[int] = 1
    total: Optional[float] = None

    class Config:
        from_attributes = True

class OrderPayment(BaseModel):
    id: Optional[str] = None
    order_id: str
    payment_method_id: str
    status: Optional[str] = "pending"

    class Config:
        from_attributes = True

class OrderShipping(BaseModel):
    id: Optional[str] = None
    order_id: str
    address_id: str
    tracking_number: Optional[str] = None
    status: Optional[str] = "pending"
    note: Optional[str] = None

    class Config:
        from_attributes = True

class OrderList(BaseModel):
    id: Optional[str] = None
    user_id: str
    status: str
    total: Optional[float] = None

    class Config:
        from_attributes = True

class OrderSingle(BaseModel):
    id: Optional[str] = None
    status: str
    total_products: Optional[int] = 0
    tax: Optional[float] = 0.0
    total: Optional[float] = None
    items: Optional[list] = None
    payment: Optional[OrderPayment] = None
    shipping: Optional[OrderShipping] = None

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
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