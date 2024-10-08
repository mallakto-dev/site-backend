install:
	poetry install

# migrations
make-migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

show-migrations:
	poetry run python manage.py showmigrations

# development
lint:
	poetry run flake8 app --exclude=settings.py,app/orders/apps.py

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=app/* --omit=app/settings.py
	poetry run coverage xml --include=app/* --omit=app/settings.py

shell:
	poetry run python manage.py shell

dev:
	poetry run python manage.py runserver 0.0.0.0:8000