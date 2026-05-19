from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from djongo import models

from django.conf import settings
from django.db import connection

from bson.objectid import ObjectId

from django.apps import apps

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data from collections
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        db = connection.cursor().db_conn
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample users
        users = [
            {"name": "Tony Stark", "email": "tony@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "steve@marvel.com", "team": "marvel"},
            {"name": "Bruce Wayne", "email": "bruce@dc.com", "team": "dc"},
            {"name": "Clark Kent", "email": "clark@dc.com", "team": "dc"},
        ]
        self.stdout.write(self.style.SUCCESS('Inserting users...'))
        db.users.insert_many(users)

        # Sample teams
        teams = [
            {"name": "marvel", "members": ["tony@marvel.com", "steve@marvel.com"]},
            {"name": "dc", "members": ["bruce@dc.com", "clark@dc.com"]},
        ]
        self.stdout.write(self.style.SUCCESS('Inserting teams...'))
        db.teams.insert_many(teams)

        # Sample activities
        activities = [
            {"user_email": "tony@marvel.com", "activity": "Running", "duration": 30},
            {"user_email": "steve@marvel.com", "activity": "Cycling", "duration": 45},
            {"user_email": "bruce@dc.com", "activity": "Swimming", "duration": 25},
            {"user_email": "clark@dc.com", "activity": "Flying", "duration": 60},
        ]
        self.stdout.write(self.style.SUCCESS('Inserting activities...'))
        db.activities.insert_many(activities)

        # Sample leaderboard
        leaderboard = [
            {"team": "marvel", "points": 75},
            {"team": "dc", "points": 85},
        ]
        self.stdout.write(self.style.SUCCESS('Inserting leaderboard...'))
        db.leaderboard.insert_many(leaderboard)

        # Sample workouts
        workouts = [
            {"user_email": "tony@marvel.com", "workout": "Bench Press", "reps": 10},
            {"user_email": "steve@marvel.com", "workout": "Push Ups", "reps": 20},
            {"user_email": "bruce@dc.com", "workout": "Pull Ups", "reps": 15},
            {"user_email": "clark@dc.com", "workout": "Squats", "reps": 25},
        ]
        self.stdout.write(self.style.SUCCESS('Inserting workouts...'))
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
