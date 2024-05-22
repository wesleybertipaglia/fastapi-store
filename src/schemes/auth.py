from pydantic import BaseModel
from typing import Optional

class SignUP(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class SignIN(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class Delete(BaseModel):
    password: str

    class Config:
        orm_mode = True