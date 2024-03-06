import random

from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker

from employee.models import Employee, Position

fake = Faker()


class Command(BaseCommand):
    help = 'Seed the database with dummy Employee data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of employees to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        seeder = Seed.seeder()

        positions = Position.objects.all()

        if not positions:
            self.stdout.write(self.style.ERROR('There is no positions. Create positions first!'))

        seeder.add_entity(Employee, total, {
            'first_name': lambda x: fake.first_name(),
            'last_name': lambda x: fake.last_name(),
            'middle_name': lambda x: fake.first_name(),
            'position': lambda x: random.choice(positions),
            'hire_date': lambda x: fake.date_between(start_date='-5y', end_date='today'),
            'email': lambda x: fake.email(),
        })

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {total} employees'))
