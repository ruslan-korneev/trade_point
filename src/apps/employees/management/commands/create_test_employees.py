from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker

from apps.employees.models import Employee



FAKE = Faker('ru_RU')


class Command(BaseCommand):
    help = "Create fake test employee"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Processing... 🚀'))

        # Create test employee's data
        names = [FAKE.unique.name() for _ in range(settings.TEST_EMPLOYEE_QUANTITY)]
        phones = [FAKE.unique.phone_number() for _ in range(settings.TEST_EMPLOYEE_QUANTITY)]

        # Create test employees
        for name, phone in zip(names, phones):
            Employee.objects.create(name=name, phone=phone)

        self.stdout.write(self.style.SUCCESS('Successfully created 🎉'))
