from rest_framework import permissions
from .models import Team, TeamMember
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from accounts.models import User

class IsOwnerOrAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        #print(request.user," ",obj.owner)
        return obj.owner == request.user or request.user.is_staff


class IsTeamOwnerOrAdmin(permissions.BasePermission):
    """ Only the team owner can add, delete and update members"""
    def has_permission(self, request, view):
        team = Team.objects.get(id=view.kwargs['teamid'])
        return request.method in permissions.SAFE_METHODS or team.owner==request.user or request.user.is_staff
    
    def has_object_permission(self, request, view, obj):
        team = Team.objects.get(id=obj.team.id)
        print(team.owner," ",request.user)
        return request.method in permissions.SAFE_METHODS or team.owner == request.user or request.user.is_staff


class IsTeamMemberOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            team = Team.objects.get(id=view.kwargs['teamid'])
            user = User.objects.get(email=request.user)
            print(user.id)
            member = TeamMember.objects.get(team=view.kwargs['teamid'],member=user.id)
        except ObjectDoesNotExist:
            member=None
        print(member,' ',view.kwargs['teamid'],' ',request.user)
        return member!=None or team.owner==request.user or request.user.is_staff 
 
    def has_object_permission(self, request, view, obj):
        try:
            team = Team.objects.get(id=obj.team.id)
            user = User.objects.get(email=request.user)
            print(user.id)
            member = TeamMember.objects.get(team=view.kwargs['teamid'],member=user.id)
        except ObjectDoesNotExist:
            member=None
        print(member,' ',view.kwargs['teamid'],' ',request.user)
        return member!=None or team.owner == request.user or request.user.is_staff