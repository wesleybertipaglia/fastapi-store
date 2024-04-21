from sqlalchemy import Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base

class UserModel (Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(100))

    products: Mapped['ProductModel'] = relationship(back_populates='user', lazy='selectin')
    orders: Mapped['OrderModel'] = relationship(back_populates='user', lazy='selectin')
