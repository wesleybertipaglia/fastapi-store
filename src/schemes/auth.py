from pydantic import BaseModel
from typing import Optional

class SignUP(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    password: str
    name: Optional[str] = None    
    bio: Optional[str] = None
    avatar: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        from_attributes = True

class SignIN(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True

class Delete(BaseModel):
    password: str

    class Config:
        from_attributes = True