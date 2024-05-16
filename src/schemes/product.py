from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    price: float
    available: bool = False
    user_id: Optional[str] = None

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    available: Optional[bool] = None
    user_id: Optional[str] = None

    class Config:
        orm_mode = True

class ProductPublic(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    description: Optional[str] = None

    class Config:
        orm_mode = True

class ProductPrivate(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    price: float
    available: bool = False
    user_id: str

    class Config:
        orm_mode = True