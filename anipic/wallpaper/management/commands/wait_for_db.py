from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as psycopg2OpError
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database")
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2OpError, OperationalError):
                self.stdout.write("Unable to connect to the Database, Retrying in 5 sec")
                time.sleep(5)
        self.stdout.write(self.style.SUCCESS("Database Ready"))