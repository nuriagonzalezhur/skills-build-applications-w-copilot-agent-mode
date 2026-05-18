from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', first_name='Steve', last_name='Rogers'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password', first_name='Diana', last_name='Prince'),
        ]

        # Create activities
        Activity.objects.create(user='ironman', activity_type='Running', duration=30)
        Activity.objects.create(user='batman', activity_type='Cycling', duration=45)
        Activity.objects.create(user='wonderwoman', activity_type='Swimming', duration=60)
        Activity.objects.create(user='captainamerica', activity_type='Rowing', duration=25)

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='batman', points=90)
        Leaderboard.objects.create(user='wonderwoman', points=110)
        Leaderboard.objects.create(user='captainamerica', points=80)

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        Workout.objects.create(name='Flight Training', description='Aerobic and flight skills')
        Workout.objects.create(name='Stealth Ops', description='Stealth and agility drills')
        Workout.objects.create(name='Shield Mastery', description='Shield skills and defense')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
