from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    price: float
    available: Optional[bool] = False
    stock: Optional[int] = 0

    class Config:
        from_attributes = True

class ProductList(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    price: float
    available: Optional[bool] = False
    stock: Optional[int] = 0

    class Config:
        from_attributes = True

class ProductSingle(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    price: float
    available: Optional[bool] = False
    stock: Optional[int] = 0

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    price: float
    available: Optional[bool] = False
    stock: Optional[int] = 0

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    user_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    price: Optional[float] = None
    available: Optional[bool] = None
    stock: Optional[int] = None

    class Config:
        from_attributes = True