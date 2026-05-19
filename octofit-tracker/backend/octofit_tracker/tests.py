from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='test')
        self.assertEqual(user.name, 'Test User')

    def test_team_creation(self):
        team = Team.objects.create(name='test', members=['test@example.com'])
        self.assertEqual(team.name, 'test')

    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='test@example.com', activity='Test', duration=10)
        self.assertEqual(activity.activity, 'Test')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='test', points=100)
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(user_email='test@example.com', workout='Test', reps=5)
        self.assertEqual(workout.reps, 5)
