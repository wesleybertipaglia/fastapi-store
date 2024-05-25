from sqlalchemy.orm import Session
from src.config.database import get_db

from .UserSeeder import UserSeeder
from .PaymentMethodSeeder import PaymentMethodSeeder
from .AddressSeeder import AddressSeeder
from .ProductSeeder import ProductSeeder
from .OrderSeeder import OrderSeeder

def main():
    db_gen = get_db()
    db: Session = next(db_gen)

    try:
        UserSeeder(db, "./src/seed/data/users.json").seed()
        PaymentMethodSeeder(db, "./src/seed/data/payment_methods.json").seed()
        AddressSeeder(db, "./src/seed/data/addresses.json").seed()
        ProductSeeder(db, "./src/seed/data/products.json").seed()
        OrderSeeder(db, "./src/seed/data/orders.json").seed()
    except Exception as e:        
        print("Error: ", e)
    finally:
        db_gen.close()

if __name__ == "__main__":
    main()