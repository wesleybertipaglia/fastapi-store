from pydantic import BaseModel
from typing import Optional

class PaymentMethod(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True

class PaymentMethodUpdate(BaseModel):
    user_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True

class PaymentMethodList(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True

class PaymentMethodGet(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True