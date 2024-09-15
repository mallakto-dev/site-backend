install:
	poetry install

# migrations
make-migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

# development
lint:
	poetry run flake8 site_backend --exclude=settings.py

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=site_backend/* --omit=site_backend/settings.py
	poetry run coverage xml --include=site_backend/* --omit=site_backend/settings.py

shell:
	poetry run python manage.py shell

dev:
	poetry run python manage.py runserver