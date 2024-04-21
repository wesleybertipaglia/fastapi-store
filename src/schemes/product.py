from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float
    available: bool = False
    user_id: int

    class Config:
        orm_mode = True

class ProductResponse(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    available: Optional[bool] = None
    user_id: Optional[int] = None

    class Config:
        orm_mode = True
