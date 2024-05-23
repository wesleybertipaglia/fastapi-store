from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id: Optional[str] = None
    user_id: str
    status: str
    total_products: Optional[int] = 0
    tax: Optional[float] = 0.0
    total: Optional[float] = None
    items: Optional[list] = None

    class Config:
        orm_mode = True


class OrderList(BaseModel):
    id: Optional[str] = None
    user_id: str
    status: str
    total_products: Optional[int] = 0
    tax: Optional[float] = 0.0
    total: Optional[float] = None

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    status: str
    total_products: int
    tax: Optional[float] = 0.0
    total: Optional[float] = None
    items: Optional[list] = None

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

class OrderCreate(BaseModel):
    status: Optional[str] = "pending"
    items: list[OrderItem]

    class Config:
        orm_mode = True