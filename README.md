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
To access the API documentation, run the application and go to the following URL:
[localhost:8000/docs](http://localhost:8000/docs)

Or you can see the documentation in [endpoints.md](/docs/endpoints.md)

## 🧩 Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Passlib](https://passlib.readthedocs.io/en/stable/)
- [Pytest](https://docs.pytest.org/en/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)

## 📜 License

This repository is licensed under the [MIT]. See the [LICENSE](LICENSE) file for details.

[Back to top](#store-api)