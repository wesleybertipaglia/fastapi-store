from pydantic import BaseModel
from typing import Optional

class SignUP(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class SignIN(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True