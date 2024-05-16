# 🚀 Project Structure

Inside this project, you'll see the following folders and files:

```text
├── alembic/
├── src/
│   ├── config/
│   ├── jobs/
│   ├── middlewares/
│   ├── models/
│   ├── providers/
│   ├── repository/
│   ├── routes/
│   └── schemes/
├── venv/
├── .gitignore
├── alembic.ini
├── database.db
├── main.py
├── Makefile
├── README.md
└── requirements.txt
```

There are several key components in this project:
- The `alembic` folder contains the database migration scripts. 
- The `src` folder contains the source code of the API. 
    - The `config` folder contains the configuration files. 
    - The `jobs` folder contains the background jobs. 
    - The `middlewares` folder contains the middleware functions. 
    - The `models` folder contains the database models. 
    - The `providers` folder contains the service providers. 
    - The `repository` folder contains the repository classes. 
    - The `routes` folder contains the API routes. 
    - The `schemes` folder contains the request and response schemes.
- The `venv` folder contains the virtual environment.
- The `.gitignore` file specifies which files and directories to ignore.
- The `alembic.ini` file contains the Alembic configuration.
- The `database.db` file is the SQLite database.
- The `main.py` file is the entry point of the API.
- The `Makefile` contains the commands to run the API.
- The `README.md` file contains the documentation.
- The `requirements.txt` file contains the dependencies.