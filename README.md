# 🏪 Store API
A Restful API for managing an online store, built using the FastAPI framework.

### Features:

- ✅ Sign-up & Sign-in
- ✅ Create and Customize your profile
- ✅ Create, Update, Delete your own products
- ✅ Create, Read, Delete your own orders
- ✅ Update your own orders until it's paid
- ✅ Search and filter products
- ✅ Make and track your orders
- ✅ Rate and review products
- ✅ Get notifications about your orders

## 📚 Table of Contents
- [Getting Started](#-getting-started)
- [Commands](#-commands)
- [Endpoints](#-endpoints)
- [Tech Stack](#-tech-stack)
- [License](#-license)
- [Checklist](#-checklist)
- [Improvements](#-improvements)

To know more about the project structure, check the [structure.md](/docs/structure.md) file.

## 🤖 Getting Started
1. Clone the repository
```bash
git clone https://github.com/wesleybertipaglia/store-api.git
```

2. Initialize and Activate the virtual environment
```bash
Make init
source venv/bin/activate
```

3. Install the dependencies and init the alembic
```bash
Make setup
```

4. Run the application
```bash
Make run
```

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                    | Action                                    |
| :------------------------  | :---------------------------------------- |
| `Make init`                | Initialize the virtual enviroment         |
| `source venv/bin/activate` | Activate the virtual enviroment           |
| `Make setup`               | Install dependencies and init the alembic |
| `Make freeze`              | Update the dependencies                   |
| `Make run`                 | Starts the application                    |
| `Make alembic-revision`    | Make an alembic revision                  |
| `Make alembic-upgrade`     | Make an alembic upgrade                   |

To know more about the commands, check the [commands.md](/docs/commands.md) file.

## 🪧 Endpoints
The API has the following endpoints:
- `/auth`: Sign-up and Sign-in
- `/profile`: Read, Update, Delete
- `/users`: Read
- `/products`: Create, Read, Update, Delete
- `/orders`: Create, Read, Update, Delete

To know more about the endpoints, check the [endpoints.md](/docs/endpoints.md) file, or access the API documentation in the following URL:
[localhost:8000/docs](http://localhost:8000/docs)

## 🧩 Tech Stack
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/) and [Adminer](https://www.adminer.org/)

To know more about the tech stack, check the [tech-stack.md](/docs/tech-stack.md) file.

## ☑️ Cheklist

The following checklist can be used to track the project progress:

- [x] Authentication
- [x] Authorization
- [x] Documentation
- [ ] Tests
- [ ] Docker
- [ ] CI/CD
- [ ] Deploy
- [ ] Monitoring

## 🚀 Improvements

The following improvements can be made to the project:

- [ ] Add avatar, username, bio to profiles
- [ ] Implement payment methods
- [ ] Change ids from int to uuid
- [ ] Add address, contact to users
- [ ] Implement roles and permissions to users
- [ ] Add stock, category, tags, images to products
- [ ] Implement reviews and rating to products
- [ ] Add coupon, tax, fee, discount to orders
- [ ] Implement order status, payment, items
- [ ] Add notifications to users
- [ ] Implement search and filter to products
- [ ] Add pagination, limit, offset to endpoints

## 📜 License

This repository is licensed under the [MIT]. See the [LICENSE](LICENSE) file for details.

[Back to top](#store-api)