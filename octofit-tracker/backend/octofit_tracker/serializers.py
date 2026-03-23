from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return data

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    team = TeamSerializer(read_only=True)
    team_id = ObjectIdField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'team', 'team_id']

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = ObjectIdField(write_only=True, required=False)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'type', 'duration', 'distance', 'timestamp']

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    suggested_for = TeamSerializer(read_only=True)
    suggested_for_id = ObjectIdField(write_only=True, required=False)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for', 'suggested_for_id']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = ObjectIdField(write_only=True, required=False)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'score']
