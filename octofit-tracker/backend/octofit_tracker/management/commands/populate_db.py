from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# MODELE TESTOWE (proste, bez migracji, tylko do populacji przez ORM)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user_email = models.EmailField()
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user_email = models.EmailField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Usuń stare dane
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Dodaj drużyny
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Dodaj użytkowników
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass'),
        ]

        # Dodaj aktywności
        Activity.objects.create(name='Run', user_email='ironman@marvel.com', team='Marvel')
        Activity.objects.create(name='Swim', user_email='spiderman@marvel.com', team='Marvel')
        Activity.objects.create(name='Fly', user_email='superman@dc.com', team='DC')
        Activity.objects.create(name='Drive', user_email='batman@dc.com', team='DC')

        # Dodaj leaderboard
        Leaderboard.objects.create(user_email='ironman@marvel.com', points=100)
        Leaderboard.objects.create(user_email='spiderman@marvel.com', points=80)
        Leaderboard.objects.create(user_email='batman@dc.com', points=90)
        Leaderboard.objects.create(user_email='superman@dc.com', points=120)

        # Dodaj workouty
        Workout.objects.create(name='Pushups', description='Do 50 pushups', user_email='ironman@marvel.com')
        Workout.objects.create(name='Pullups', description='Do 20 pullups', user_email='spiderman@marvel.com')
        Workout.objects.create(name='Situps', description='Do 100 situps', user_email='batman@dc.com')
        Workout.objects.create(name='Squats', description='Do 200 squats', user_email='superman@dc.com')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
