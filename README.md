# Simple Store API
This is a simple API for managing a store. It allows you to perform basic CRUD operations on products and orders.

## Installation

1. Clone the repository: `git clone https://github.com/wesleybertipaglia/simple-store-api.git`
2. Install dependencies: `make init & make setup`

## Usage

1. Start the server: `make run`
2. Access the API at: `http://localhost:8000`

## Endpoints

### Users

### Products

- `GET /products`: Get all products
- `GET /products/:id`: Get a specific product by ID
- `POST /products`: Create a new product
- `PUT /products/:id`: Update a product by ID
- `DELETE /products/:id`: Delete a product by ID

### Orders

- `GET /orders`: Get all orders
- `GET /orders/:id`: Get a specific order by ID
- `POST /orders`: Create a new order
- `PUT /orders/:id`: Update an order by ID
- `DELETE /orders/:id`: Delete an order by ID

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).