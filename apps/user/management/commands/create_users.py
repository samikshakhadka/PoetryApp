from faker import Faker
from apps.user.models import CustomUser
from django.core.management.base import BaseCommand
import uuid

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        for i in range(total):
            email = fake.email()
            first_name = fake.first_name()
            last_name = fake.last_name()
            password = 'Asdfghjkl@123'
            verification_token = uuid.uuid4()

            CustomUser.objects.create_user( email=email, password=password,first_name=first_name,
                last_name=last_name,verification_token=verification_token)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {i + 1} with email {email}'))
