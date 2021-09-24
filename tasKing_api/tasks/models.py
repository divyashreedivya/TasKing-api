from django.db import models
from django.conf import settings
from django.db.models.base import Model

class PersonalTask(models.Model):
    NOT_DONE = 'ND'
    IN_PROGRESS = 'P'
    DONE = 'D'
    status_choices = [
        (NOT_DONE,'Not done'),
        (IN_PROGRESS,'In progress'),
        (DONE,'Done')
    ]

    title = models.CharField(max_length=256)
    description = models.TextField()
    due_time = models.DateTimeField()
    category = models.CharField(max_length=256)
    priority = models.IntegerField()
    status = models.CharField(max_length=100,choices=status_choices,default=NOT_DONE)
    task_public = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='personaltasks',on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=256)
    info = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='teams',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    team = models.ForeignKey('Team',related_name='team',on_delete=models.CASCADE)
    member = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='member',on_delete=models.CASCADE)


class TeamTask(models.Model):
    NOT_DONE = 'ND'
    IN_PROGRESS = 'P'
    DONE = 'D'
    status_choices = [
        (NOT_DONE,'Not done'),
        (IN_PROGRESS,'In progress'),
        (DONE,'Done')
    ]

    title = models.CharField(max_length=256)
    description = models.TextField()
    due_time = models.DateTimeField()
    team = models.ForeignKey('Team',on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=status_choices,default=NOT_DONE)

    def __str__(self):
        return self.title
