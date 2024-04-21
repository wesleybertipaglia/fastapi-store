from sqlalchemy import Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base

class ProductModel(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float)
    available: Mapped[bool] = mapped_column(Boolean)

    user: Mapped['UserModel'] = relationship(back_populates='products')
    orders: Mapped['OrderModel'] = relationship(back_populates='product')
