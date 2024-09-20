#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
make install

# Apply any outstanding database migrations
make migrate

#flush to database
poetry run python manage.py loaddata dumpdb.jdon.gz