# project
init: 
	@python3 -m venv venv

setup:	
	@pip3 install -r requirements.txt

freeze:
	@pip3 freeze > requirements.txt

run:	
	@uvicorn main:app --reload

test:
	@pytest

# Docker
docker-compose-up:
	@docker compose up -d

docker-compose-down:
	@docker compose down


# Alembic
alembic-init:
	@alembic init alembic

alembic-migrate:
	@alembic migrate

alembic-upgrade:
	@alembic upgrade head

alembic-downgrade:
	@alembic downgrade -1

alembic-history:
	@alembic history

alembic-current:
	@alembic current

alembic-revision:
	@alembic revision --autogenerate