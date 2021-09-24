from django.urls.conf import include
from django.urls import path
from . import views
from rest_framework import routers
from .models import PersonalTask,Team, TeamMember, TeamTask

router = routers.DefaultRouter()
router.register('personaltasks',views.PersonalTasksViewSet,basename=PersonalTask)
router.register('teams',views.TeamViewSet,basename=Team)
router.register(r'teams/(?P<teamid>\d+)/members',views.TeamMemberViewSet,basename=TeamMember)
router.register(r'teams/(?P<teamid>\d+)/tasks',views.TeamTaskViewSet,basename=TeamTask)

urlpatterns=[
    path('',include(router.urls)),
]