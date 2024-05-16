from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base
from uuid import uuid4

class UserModel (Base):
    __tablename__ = 'users'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=str(uuid4()))
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(100))

    products: Mapped['ProductModel'] = relationship(back_populates='user', lazy='selectin')
    orders: Mapped['OrderModel'] = relationship(back_populates='user', lazy='selectin')
