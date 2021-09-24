from django.contrib import admin
from .models import Team,TeamTask,PersonalTask,TeamMember

admin.site.register(PersonalTask)
admin.site.register(TeamTask)
admin.site.register(Team)
admin.site.register(TeamMember)
