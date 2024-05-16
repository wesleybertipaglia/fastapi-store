# 🧞 Commands

All commands are run from the root of the project, from a terminal:


## Project commands

| Command                    | Action                                    |
| :------------------------  | :---------------------------------------- |
| `make init`                | Initialize the virtual enviroment         |
| `source venv/bin/activate` | Activate the virtual enviroment           |
| `make setup`               | Install dependencies and init the alembic |
| `make freeze`              | Update the dependencies                   |
| `make run`                 | Starts the application                    |
| `make test`                | Run the tests                             |

## Docker commands

| Command                    | Action                                    |
| :------------------------  | :---------------------------------------- |
| `make docker-compose-up`   | Run docker compose                        |
| `make docker-compose-down` | Shutdown the docker                       |

## Alembic commands

| Command                    | Action                                    |
| :------------------------  | :---------------------------------------- |
| `make alembic-init`        | Init the alembic                          |
| `make alembic-migrate`     | Make an alembic migration                 |
| `make alembic-upgrade`     | Make an alembic upgrade                   |
| `make alembic-downgrade`   | Make an alembic downgrade                 |
| `make alembic-history`     | Show the alembic history                  |
| `make alembic-current`     | Show the current migration version        |
| `make alembic-revision`    | Make an alembic revision                  |