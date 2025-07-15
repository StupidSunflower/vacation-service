import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

def setup_database():
    with connection.cursor() as cursor:
        print("Database setup complete - use migrations to create tables")

if __name__ == '__main__':
    setup_database()