from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    username: Optional[str]
    email: str
    password: str

    class Config:
        orm_mode = True

class UserPrivate(BaseModel):
    id: Optional[str] = None
    username: Optional[str]
    name: Optional[str] = None
    email: str

    class Config:
        orm_mode = True

class UserPublic(BaseModel):
    id: Optional[str] = None
    username: Optional[str] = None
    name: Optional[str] = None
    
    class Config:
        orm_mode = True