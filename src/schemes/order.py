from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id: Optional[int] = None
    user_id: int
    product_id: int
    quantity: int
    total: Optional[float] = None

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    product_id: Optional[int] = None
    quantity: Optional[int] = None

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    product_id: Optional[int] = None
    quantity: Optional[int] = None

    class Config:
        orm_mode = True