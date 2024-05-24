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
- [Getting Started](#getting-started)
- [Commands](#-commands)
- [Tech Stack](#-tech-stack)
- [License](#-license)
- [Checklist](#-checklist)

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

> 🚀 Open your browser and go to [http://localhost:8000](http://localhost:8000) to see the api in action.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                    | Action                                    |
| :------------------------  | :---------------------------------------- |
| `make init`                | Initialize the virtual enviroment         |
| `source venv/bin/activate` | Activate the virtual enviroment           |
| `make setup`               | Install dependencies and init the alembic |
| `make freeze`              | Update the dependencies                   |
| `make run`                 | Starts the application                    |
| `make alembic-migrate`     | Make an alembic migration                 |
| `make alembic-upgrade`     | Make an alembic upgrade                   |
| `make alembic-downgrade`   | Make an alembic downgrade                 |

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
- [SQLite](https://www.sqlite.org/)

To know more about the tech stack, check the [stack.md](/docs/stack.md) file.

## ☑️ Cheklist

The following checklist can be used to track the project progress:

- [x] Authentication
- [x] Authorization
- [x] Documentation
- [ ] Tests
- [x] Docker
- [ ] CI/CD
- [ ] Deploy
- [ ] Monitoring

## 📜 License

This repository is licensed under the [MIT]. See the [LICENSE](LICENSE) file for details.

[Back to top](#store-api)