from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base
from uuid import uuid4

class PaymentMethodModel(Base):
    __tablename__ = 'payment_methods'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey('users.id'))
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False, )
    
    user: Mapped['UserModel'] = relationship('UserModel', back_populates='payment_methods')
    order_payment: Mapped['OrderPaymentModel'] = relationship('OrderPaymentModel', back_populates='payment_method')