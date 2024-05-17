from sqlalchemy import Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base
from uuid import uuid4

class OrderModel(Base):
    __tablename__ = 'orders'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id'))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    total: Mapped[float] = mapped_column(Float, nullable=False)

    user: Mapped['UserModel'] = relationship('UserModel', back_populates='orders')
    product: Mapped['ProductModel'] = relationship('ProductModel', back_populates='orders')