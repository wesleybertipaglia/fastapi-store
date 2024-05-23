from sqlalchemy import Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.config.database import Base
from uuid import uuid4

class AddressModel(Base):
    __tablename__ = 'addresses'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey('users.id'))
    address: Mapped[str] = mapped_column(String, nullable=False)
    city: Mapped[str] = mapped_column(String, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False)
    zip_code: Mapped[str] = mapped_column(String, nullable=False)
    country: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped['UserModel'] = relationship('UserModel', back_populates='addresses')
    order_shipping: Mapped['OrderShippingModel'] = relationship('OrderShippingModel', back_populates='address')