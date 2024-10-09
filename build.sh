#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
make install

# Apply any outstanding database migrations
make migrate

# Convert static asset files
python manage.py collectstatic --no-input

#flush to database
poetry run python manage.py loaddata dumpdb.json.gz