from django.db import models
from django.contrib.auth.models import AbstractUser
from djongo import models as djongo_models
from bson import ObjectId

class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    team = djongo_models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = djongo_models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # in minutes
    distance = models.FloatField()  # in kilometers
    timestamp = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = djongo_models.ForeignKey(Team, on_delete=models.CASCADE, related_name='workouts')

class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = djongo_models.ForeignKey('User', on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()
