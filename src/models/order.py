from sqlalchemy import Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base
from uuid import uuid4

class OrderModel(Base):
    __tablename__ = 'orders'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey('users.id'))
    status: Mapped[str] = mapped_column(String, nullable=False, default='pending')
    total_products: Mapped[int] = mapped_column(Integer, nullable=False)
    tax: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    total: Mapped[float] = mapped_column(Float, nullable=False)

    user: Mapped['UserModel'] = relationship('UserModel', back_populates='orders')
    order_items: Mapped['OrderItemsModel'] = relationship('OrderItemsModel', back_populates='order')
    order_payment: Mapped['OrderPaymentModel'] = relationship('OrderPaymentModel', back_populates='order')

class OrderItemsModel(Base):
    __tablename__ = 'order_items'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    order_id: Mapped[str] = mapped_column(String, ForeignKey('orders.id'))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id'))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    total: Mapped[float] = mapped_column(Float, nullable=False)

    order: Mapped['OrderModel'] = relationship('OrderModel', back_populates='order_items')
    product: Mapped['ProductModel'] = relationship('ProductModel', back_populates='orders')

class OrderPaymentModel(Base):
    __tablename__ = 'order_payment'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    order_id: Mapped[str] = mapped_column(String, ForeignKey('orders.id'))
    payment_method_id: Mapped[str] = mapped_column(String, ForeignKey('payment_methods.id'))
    status: Mapped[str] = mapped_column(String, nullable=False)

    order: Mapped['OrderModel'] = relationship('OrderModel', back_populates='order_payment')
    payment_method: Mapped['PaymentMethodModel'] = relationship('PaymentMethodModel', back_populates='order_payment')