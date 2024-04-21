from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True