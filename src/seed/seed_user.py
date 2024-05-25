import json
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.repository.user import UserRepository
from src.schemes.auth import SignUP

class UserSeeder:
    def __init__(self, db: Session, data_file: str):
        self.db = db
        self.repository = UserRepository(self.db)
        self.data_file = data_file
        self.data = []
    
    def seed(self):
        with open(self.data_file, "r") as file:
            data = json.load(file)
            self.data = data

        if not self.data:
            return
        for item in self.data:
            try:
                user = SignUP(**item)
                self.repository.create(user)
                print(f"User {user.email} created successfully")
            except Exception as e:
                print(f"Error creating entry: {e}")

def main():
    db: Session = next(get_db())
    try:
        seeder = UserSeeder(db, "./src/seed/data/users.json")
        seeder.seed()
    except Exception as e:
        print(f"Error loading seed data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()