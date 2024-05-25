import json
from sqlalchemy.orm import Session
from src.repository.user import UserRepository
from src.schemes.auth import SignUP

class UserSeeder:
    def __init__(self, db: Session, data_file: str):
        self.repository = UserRepository(db)
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
                user = SignUP(**item)
                self.repository.create(user)
                print(f"New user {user.id} created successfully")
            except Exception as e:
                print(f"Error creating entry: {e}")