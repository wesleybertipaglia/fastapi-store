from sqlalchemy import Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base

class OrderModel(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id'))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    total: Mapped[float] = mapped_column(Float, nullable=False)

    user: Mapped['UserModel'] = relationship(back_populates='orders')
    product: Mapped['ProductModel'] = relationship(back_populates='orders')