from rest_framework import generics, serializers,viewsets
from .models import PersonalTask,Team,TeamTask,TeamMember
from .serializers import PersonalTaskSerializer, TeamMemberSerializer,TeamSerializer,TeamTaskSerializer
from .permissions import IsOwnerOrAdmin, IsTeamMemberOrAdmin,IsTeamOwnerOrAdmin
from rest_framework.response import Response

#Viewset for personal tasks
class PersonalTasksViewSet(viewsets.ModelViewSet):
    """ To view a user's tasks ,add ,update and delete a task """
    serializer_class = PersonalTaskSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return PersonalTask.objects.filter(owner=self.request.user)


#View set for teams
#Member view needs to be fixed
class TeamViewSet(viewsets.ModelViewSet):
    """ List, create, retrieve, update and delete teams"""
    serializer_class = TeamSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Team.objects.filter(owner=self.request.user)

    
class TeamMemberViewSet(viewsets.ModelViewSet):
    """To get, add, update or delete team members"""
    serializer_class = TeamMemberSerializer

    def perform_create(self, serializer):
        team = Team.objects.get(id=self.kwargs['teamid'])
        serializer.save(team=team)      

    def get_queryset(self):
        teamid = self.kwargs['teamid']
        return TeamMember.objects.filter(team=teamid)

    def get_permissions(self):
        permission_classes = []
        if self.action=='list' or self.action=='retrieve':
            #Any member can view other members in the team
            permission_classes = [IsTeamMemberOrAdmin]
        else:
            #Only the team owner can add, update or delete team members
            permission_classes = [IsTeamOwnerOrAdmin]
        return [permission() for permission in permission_classes]
        
#Viewset for team tasks
class TeamTaskViewSet(viewsets.ModelViewSet):
    """Viewset that allows any team member to get, add, update or delete team tasks"""
    serializer_class = TeamTaskSerializer
    permission_classes = [IsTeamMemberOrAdmin]

    def perform_create(self, serializer):
        team = Team.objects.get(id=self.kwargs['teamid'])
        serializer.save(team=team) 

    def get_queryset(self):
        teamid = self.kwargs['teamid']
        return TeamTask.objects.filter(team=teamid)