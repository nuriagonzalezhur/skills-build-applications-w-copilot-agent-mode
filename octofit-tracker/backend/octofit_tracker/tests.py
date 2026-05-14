from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', activity_type='Running', duration=30)
        self.assertEqual(activity.activity_type, 'Running')

    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='testuser', points=100)
        self.assertEqual(lb.points, 100)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.username, 'testuser')
