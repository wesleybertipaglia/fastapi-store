from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.order import OrderItemsModel

class SalesRepository():
    def __init__(self, db: Session):
        self.db = db    
    
    def list(self, user_id: str, skip: int, limit: int):
        try:
            return self.db.query(OrderItemsModel).filter(OrderItemsModel.seller_id == user_id).offset(skip).limit(limit).all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while fetching your request: {e}")
        
    def get(self, id: str, user_id: str):
        try:
            return self.db.query(OrderItemsModel).filter(OrderItemsModel.id == id, OrderItemsModel.seller_id == user_id).first()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while fetching your request: {e}")