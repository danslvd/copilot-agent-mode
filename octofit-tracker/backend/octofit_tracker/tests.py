from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

class UserTestCase(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(username='test', email='test@example.com')
        self.assertEqual(user.email, 'test@example.com')

class TeamTestCase(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityTestCase(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name='Test Activity', user_email='test@example.com')
        self.assertEqual(activity.name, 'Test Activity')

class LeaderboardTestCase(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Test Team', points=10)
        self.assertEqual(lb.points, 10)

class WorkoutTestCase(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')
