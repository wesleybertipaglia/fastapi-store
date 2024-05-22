# 🪧 Endpoints

The API has the following endpoints:

### Auth

| Route                        | Action                                  |
| :--------------------------- | :-------------------------------------- |
| `POST /auth/up`              | Sign-up                                 |
| `POST /auth/in`              | Sign-in                                 |
| `POST /auth/out`             | Sign-out                                |
| `DELETE /auth/delete`        | Delete your account                     |

### Profile

| Route                        | Action                                  |
| :--------------------------- | :-------------------------------------- |
| `GET /profile`               | Get your profile                        |
| `PUT /profile`               | Update your profile                     |

### Users

| Route                        | Action                                  |
| :--------------------------- | :-------------------------------------- |
| `GET /users/:filters`        | Get all users  (filter are optional)    |
| `GET /users/:id`             | Get a specific user by ID               |

### Products

| Route                        | Action                                  |
| :--------------------------- | :-------------------------------------- |
| `GET /products/:filters`     | Get all products (filter are optional)  |
| `GET /products/:id`          | Get a specific product by ID            |
| `POST /products`             | Create a new product                    |
| `PUT /products/:id`          | Update a product by ID                  |
| `DELETE /products/:id`       | Delete a product by ID                  |


### Orders

| Route                        | Action                                  |
| :--------------------------- | :-------------------------------------- |
| `GET /orders`                | Get all your orders                     |
| `GET /orders/:id`            | Get a specific order by ID              |
| `POST /orders`               | Create a new order                      |
| `PUT /orders/:id`            | Update a order by ID                    |
| `DELETE /orders/:id`         | Delete a order by ID                    |