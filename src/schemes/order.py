from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id: Optional[str] = None
    user_id: str
    product_id: str
    quantity: int
    tax: Optional[float] = None
    total: Optional[float] = None

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    product_id: Optional[str] = None
    quantity: Optional[int] = None

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    product_id: Optional[str] = None
    quantity: Optional[int] = None

    class Config:
        orm_mode = True