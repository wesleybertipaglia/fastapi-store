import json
from sqlalchemy.orm import Session
from src.repository.payment import PaymentMethodRepository
from src.schemes.payment import PaymentMethodCreate

class PaymentMethodSeeder:
    def __init__(self, db: Session, data_file: str):
        self.repository = PaymentMethodRepository(db)
        self.data_file = data_file
        self.data = []
    
    def seed(self):
        try:
            with open(self.data_file, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            return
        except json.JSONDecodeError:
            print(f"Error: The file {self.data_file} is not a valid JSON file.")
            return

        if not self.data:
            print("No data to seed.")
            return

        for item in self.data:
            try:
                user_id: str = item.pop("user_id")
                payment_method = PaymentMethodCreate(**item)                
                self.repository.create(user_id=user_id, payment_method=payment_method)
                print(f"New payment method {payment_method.id} created successfully")
            except Exception as e:
                print(f"Error creating entry: {e}")