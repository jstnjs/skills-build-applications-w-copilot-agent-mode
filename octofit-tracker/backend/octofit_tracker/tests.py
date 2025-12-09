from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, LeaderboardEntry

class BasicModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.team = Team.objects.create(name='Test Team')
        self.activity = Activity.objects.create(user=self.user, team=self.team, type='run', duration=30, calories=200, date='2023-01-01')
        self.workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy', suggested_for='Everyone')
        self.leaderboard = LeaderboardEntry.objects.create(user=self.user, team=self.team, total_calories=200, total_duration=30, rank=1)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'run')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Pushups')

    def test_leaderboard_entry(self):
        self.assertEqual(self.leaderboard.rank, 1)
