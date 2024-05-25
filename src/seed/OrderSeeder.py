import json
from sqlalchemy.orm import Session
from src.repository.order import OrderRepository
from src.schemes.order import OrderCreate, OrderItem, OrderShipping, OrderPayment

class OrderSeeder:
    def __init__(self, db: Session, data_file: str):
        self.repository = OrderRepository(db)
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
                items_data = item.pop("items")
                payment_data = item.pop("payment")
                shipping_data = item.pop("shipping")
                                
                items = [OrderItem(**item) for item in items_data]
                payment = OrderPayment(**payment_data)
                shipping = OrderShipping(**shipping_data)
                order = OrderCreate(id=item["id"], items=items, shipping=shipping, payment=payment)

                self.repository.create(user_id=user_id, order=order)
                print(f"New order {order.id} created successfully")
            except Exception as e:
                print(f"Error creating entry: {e}")