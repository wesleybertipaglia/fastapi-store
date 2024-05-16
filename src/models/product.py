from sqlalchemy import Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base
from uuid import uuid4

class ProductModel(Base):
    __tablename__ = 'products'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=str(uuid4()))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float)
    available: Mapped[bool] = mapped_column(Boolean)

    user: Mapped['UserModel'] = relationship(back_populates='products')
    orders: Mapped['OrderModel'] = relationship(back_populates='product')
