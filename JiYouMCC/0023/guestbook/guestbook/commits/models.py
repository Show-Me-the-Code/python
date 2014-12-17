from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField(max_length=65535)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name + ':' + self.message[:25]
