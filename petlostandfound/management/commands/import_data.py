import csv
from datetime import date
from django.core.management.base import BaseCommand
from petlostandfound.models import User, Pet, LostPetReport

class Command(BaseCommand):
    help = 'Populate data'

    def handle(self, *args, **options):
        # Create users using the predefined data
        user_1 = User.objects.create(
            name='John Doe',
            email='john@example.com'
        )

        user_2 = User.objects.create(
             name='Jane Smith',
             email='jane@example.com'
        )

        user_2 = User.objects.create(
             name='Pet Lover',
             email='petlover@example.com'
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully created users'))

        # Create pets using the predefined data
        pet_buddy = Pet.objects.create(
            name='Buddy',
            age=3,
            pet_type='dog',
            breed='Golden Retriever',
            sex='M',
            color='Gold',
            owner=User.objects.get(name='John Doe')
        )

        pet_whiskers = Pet.objects.create(
            name='Whiskers',
            age=2,
            pet_type='cat',
            breed='Persian',
            sex='F',
            color='White',
            owner=User.objects.get(name='Jane Smith')
        )

        pet_fluffy = Pet.objects.create(
            name='Fluffy',
            age=1,
            pet_type='cat',
            breed='Ragdoll',
            sex='F',
            color='Gray',
            owner=User.objects.get(name='Pet Lover')
        )

        pet_max = Pet.objects.create(
            name='Max',
            age=4,
            pet_type='dog',
            breed='Poodle',
            sex='M',
            color='Brown',
            owner=User.objects.get(name='John Doe')
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully created Pets'))

        # Create LostPetReport instances
        LostPetReport.objects.create(
            reported_by=User.objects.get(name='Jane Smith'),
            pet=pet_buddy,
            report_date=date.today(),
            last_seen_location='Central Park',
            description='Lost in the park.',
            is_found=False
        )

        LostPetReport.objects.create(
            reported_by=User.objects.get(name='Pet Lover'),
            pet=pet_fluffy,
            report_date=date.today(),
            last_seen_location='Downtown Street',
            description='Found a stray cat.',
            is_found=True
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully created reports'))