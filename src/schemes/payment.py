from pydantic import BaseModel
from typing import Optional

class PaymentMethod(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    class Config:
        from_attributes = True

class PaymentMethodList(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None

    class Config:
        from_attributes = True

class PaymentMethodSingle(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    class Config:
        from_attributes = True

class PaymentMethodCreate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    class Config:
        from_attributes = True

class PaymentMethodUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    class Config:
        from_attributes = True