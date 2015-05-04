from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    status = models.CharField(max_length=30)

    def __unicode__(self):
        return self.status


class List(models.Model):
    user = models.ForeignKey(User)
    createdate = models.DateTimeField()
    duedate = models.DateTimeField()
    detail = models.CharField(max_length=65535)
    status = models.ForeignKey(Status)

    def __unicode__(self):
        return self.detail
