from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemes.payment import PaymentMethod, PaymentMethodUpdate
from src.models.payment import PaymentMethodModel

class PaymentMethodRepository():
    def __init__(self, db: Session):
        self.db = db

    def list(self, user_id: str, skip: int, limit: int):
        try:
            return self.db.query(PaymentMethodModel).filter(PaymentMethodModel.user_id == user_id).offset(skip).limit(limit).all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while fetching your request: {e}.")

    def get(self, id: str):
        payment_method = self.db.query(PaymentMethodModel).filter(PaymentMethodModel.id == id).first()

        if not payment_method:
            raise HTTPException(status_code=404, detail="Payment method not found")
        
        return payment_method

    def create(self, user_id: str, payment_method: PaymentMethod):
        new_payment_method = PaymentMethodModel(
            user_id=user_id,
            name=payment_method.name,
            description=payment_method.description,
            type=payment_method.type
        )

        self.db.add(new_payment_method)
        self.db.commit()
        self.db.refresh(new_payment_method)
        return new_payment_method
    
    def update(self, id: str, user_id: str, payment_method: PaymentMethodUpdate):
        stored_payment_method = self.get(id)

        if stored_payment_method.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to update this payment method")

        for field in payment_method.model_dump(exclude_unset=True):
            setattr(stored_payment_method, field, getattr(payment_method, field))

        self.db.commit()
        self.db.refresh(stored_payment_method)
        return stored_payment_method

    def delete(self, id: str, user_id: str):
        stored_payment_method = self.get(id)
        
        if stored_payment_method.user_id != user_id:
            raise HTTPException(status_code=403, detail="You don't have permission to delete this payment method")
    
        self.db.delete(stored_payment_method)
        self.db.commit()
        return {"detail": "Payment method deleted"}