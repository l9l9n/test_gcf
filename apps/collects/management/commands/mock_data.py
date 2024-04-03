from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.collects.models import Collect, Payment
from faker import Faker
import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_users = 100  # создать столько-то пользователей
        num_collects = 20  # создать столько-то collects
        num_payments = 50  # Количество платежей, которые необходимо создать за каждый сбор

        # Create users
        for _ in range(num_users):
            username = fake.user_name()
            email = fake.email()
            password = 'password'
            User.objects.create_user(username=username, email=email, password=password)

        # создание collects and payments
        users = User.objects.all()
        occasions = ['birth day', 'marry']
        for _ in range(num_collects):
            author = random.choice(users)
            title = fake.catch_phrase()
            choice_occasion = random.choice(occasions)[1]
            description = fake.text()
            target_amount = random.randint(100, 1000)
            collected_amount = random.randint(0, target_amount)
            contributors_count_donations = random.randint(0, 10)
            end_date = fake.date_time_between(start_date='now', end_date='+30d')
            image_cover = 'placeholder.jpg'  # Placeholder image for now
            collect = Collect.objects.create(author=author, title=title, choice_occasion=choice_occasion,
                                             description=description, target_amount=target_amount,
                                             collected_amount=collected_amount,
                                             contributors_count_donations=contributors_count_donations,
                                             end_date=end_date, image_cover=image_cover)
            for _ in range(num_payments):
                contributor = random.choice(users)
                amount = random.randint(10, 100)
                Payment.objects.create(collect=collect, contributor=contributor, amount=amount)

        self.stdout.write(self.style.SUCCESS('Mock data has been successfully populated.'))
