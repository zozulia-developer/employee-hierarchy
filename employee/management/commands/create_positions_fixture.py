import json

from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Generate fixture data for 100 positions'

    def handle(self, *args, **kwargs):
        position_names = set()
        while len(position_names) < 100:
            position_names.add(fake.job())

        positions = []
        pos_count = 1
        for position_name in position_names:
            position_data = {
                'model': 'employee.position',
                'pk': pos_count,
                'fields': {
                    'name': position_name
                }
            }
            positions.append(position_data)
            pos_count += 1

        with open('positions.json', 'w') as f:
            json.dump(positions, f, indent=2)

        self.stdout.write(self.style.SUCCESS('Fixture data generated successfully.'))
