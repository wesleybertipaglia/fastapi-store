from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    image_url: Optional[str] = None
    price: float
    available: bool = False
    stock: int = 0
    user_id: Optional[str] = None

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    price: Optional[float] = None
    available: Optional[bool] = None
    stock: Optional[int] = None
    user_id: Optional[str] = None

    class Config:
        orm_mode = True

class ProductPublic(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    description: Optional[str] = None
    image_url: Optional[str] = None

    class Config:
        orm_mode = True

class ProductPrivate(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    image_url: Optional[str] = None
    price: float
    available: bool = False
    stock: int = 0
    user_id: str

    class Config:
        orm_mode = True