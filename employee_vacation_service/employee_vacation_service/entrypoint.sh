#!/bin/bash

set -e

# Function to check PostgreSQL using Python
check_postgres() {
  python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(
        dbname="$POSTGRES_DB",
        user="$POSTGRES_USER",
        password="$POSTGRES_PASSWORD",
        host="db"
    )
    conn.close()
except psycopg2.OperationalError:
    sys.exit(1)
sys.exit(0)
END
}

# Wait for PostgreSQL
until check_postgres; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing commands"

# Apply database migrations
python manage.py migrate

# Start server
exec "$@"