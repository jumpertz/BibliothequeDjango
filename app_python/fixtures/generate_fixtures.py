import os
import django
import json
from django.conf import settings
from faker import Faker
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projet_python2.settings")

django.setup()
settings.configure()

fake = Faker()


def generate_user_fixtures():
    users = []
    for i in range(10):
        user = User.objects.create(
            username=fake.user_name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            is_staff=False,
            is_active=True,
            date_joined=fake.date_time_between(start_date='-30y', end_date='now')
        )
        user.set_password("password")
        user.save()
        users.append(user)
    return users


def generate_admin_fixtures():
    admin = User.objects.create(
        username=fake.user_name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        is_staff=True,
        is_superuser=True,
        is_active=True,
        date_joined=fake.date_time_between(start_date='-30y', end_date='now')
    )
    admin.set_password("password")
    admin.save()
    admin.append(admin)
    return admin


# Dumps fixtures to a JSON file
out_file = open("app_python/fixtures/users.json", "w")
json.dump(generate_user_fixtures(), out_file)
json.dump(generate_admin_fixtures(), out_file)
out_file.close()
