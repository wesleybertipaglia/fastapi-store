from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    username: Optional[str]
    email: str
    password: str

    class Config:
        orm_mode = True

class UserList(BaseModel):
    id: Optional[str] = None
    username: Optional[str]
    name: Optional[str] = None

    class Config:
        orm_mode = True

class UserSingle(BaseModel):
    id: Optional[str] = None
    username: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None    
    
    class Config:
        orm_mode = True