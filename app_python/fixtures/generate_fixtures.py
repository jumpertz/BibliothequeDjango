import json
from faker import Faker


from django.contrib.auth.models import User
from django.conf import settings

settings.configure(DEBUG=True)


fake = Faker()


def generate_user():
    for user_data in users:
        try:
            user = User.objects.create_user(
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                password='password123'
            )
            user.save()
        except:
            print(f"User with username {user_data['username']} already exists")


users = [generate_user() for _ in range(10)]

filename = './app_python/fixtures/users.json'
with open(filename, 'w') as f:
    json.dump(users, f, indent=4)

print(f'{len(users)} users generated and saved to {filename}')
