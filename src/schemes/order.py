from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id: Optional[str] = None
    user_id: str
    payment_method_id: Optional[str] = None
    status: str
    total_products: Optional[int] = 0
    tax: Optional[float] = 0.0
    total: Optional[float] = None
    items: Optional[list] = None
    payment: Optional[dict] = None
    shipping: Optional[dict] = None    

    class Config:
        orm_mode = True

class OrderItem(BaseModel):
    id: Optional[str] = None
    order_id: Optional[str] = None
    product_id: str
    quantity: int
    total: Optional[float] = None

    class Config:
        orm_mode = True

class OrderPayment(BaseModel):
    id: Optional[str] = None
    order_id: Optional[str] = None
    payment_method_id: str
    status: str

    class Config:
        orm_mode = True

class OrderShipping(BaseModel):
    id: Optional[str] = None
    order_id: Optional[str] = None
    address_id: str
    tracking_number: Optional[str] = None
    status: str
    note: Optional[str] = None

    class Config:
        orm_mode = True

class OrderList(BaseModel):
    id: Optional[str] = None
    user_id: str
    status: str
    total: Optional[float] = None

    class Config:
        orm_mode = True

class OrderSingle(BaseModel):
    id: Optional[str] = None
    status: str
    total_products: Optional[int] = 0
    tax: Optional[float] = 0.0
    total: Optional[float] = None
    items: Optional[list] = None
    payment: Optional[dict] = None
    shipping: Optional[dict] = None

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    status: Optional[str] = "processing"
    items: list[OrderItem]
    payment_method_id: Optional[str] = None
    payment_status: Optional[str] = "pending"

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    status: str
    total_products: int    
    tax: Optional[float] = 0.0
    total: Optional[float] = None
    items: Optional[list] = None
    payment_method_id: Optional[str] = None

    class Config:
        orm_mode = True