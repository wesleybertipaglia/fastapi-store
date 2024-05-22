from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base
from uuid import uuid4

class UserModel (Base):
    __tablename__ = 'users'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))    
    username: Mapped[str] = mapped_column(String(14))    
    email: Mapped[str] = mapped_column(String(100))    
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(50), nullable=True)
    bio: Mapped[str] = mapped_column(String(100), nullable=True)
    avatar: Mapped[str] = mapped_column(String(100), nullable=True)
    phone: Mapped[str] = mapped_column(String(15), nullable=True)
    address: Mapped[str] = mapped_column(String(100), nullable=True)

    products: Mapped['ProductModel'] = relationship('ProductModel', back_populates='user')
    orders: Mapped['OrderModel'] = relationship('OrderModel', back_populates='user')
