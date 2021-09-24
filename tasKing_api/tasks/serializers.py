from .models import PersonalTask,Team, TeamMember,TeamTask
from rest_framework import serializers

class PersonalTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model=PersonalTask
        fields = ['id','title','owner','description','due_time','category','priority','status','task_public']

class TeamSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model=Team
        fields=['id','name','info','owner']

class TeamMemberSerializer(serializers.ModelSerializer):
    team = serializers.ReadOnlyField(source='team.id')

    class Meta:
        model = TeamMember
        fields = ['id','team','member']

class TeamTaskSerializer(serializers.ModelSerializer):
    team = serializers.ReadOnlyField(source='team.id')

    class Meta:
        model=TeamTask
        fields=['title','description','due_time','team','status']