from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from employee.models import Employee, Position

fake = Faker()


class Command(BaseCommand):
    help = 'Populate the database with 50,000 employees and 7 levels of hierarchy'

    def handle(self, *args, **kwargs):
        positions = [
            Position.objects.create(name=fake.job())
            for i in range(1, 11)
        ]

        root = Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            middle_name=fake.first_name(),
            position=positions[randint(0, len(positions) - 1)],
            hire_date=fake.date_between(start_date='-30y', end_date='today'),
            email=fake.email(),
            parent=None
        )

        self.create_hierarchy(root, 1, positions)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))

    def create_hierarchy(self, parent, level, positions):
        if level > 7:
            return

        for _ in range(10):
            employee = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                middle_name=fake.first_name(),
                position=positions[randint(0, len(positions) - 1)],
                hire_date=fake.date_between(start_date='-30y', end_date='today'),
                email=fake.email(),
                parent=parent
            )

            self.create_hierarchy(employee, level + 1, positions)
