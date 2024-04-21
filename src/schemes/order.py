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

class OrderResponse(BaseModel):
    id: Optional[int] = None
    user_id: int
    product_id: int
    quantity: int
    total: float

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    user_id: Optional[int] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    total: Optional[float] = None

    class Config:
        orm_mode = True