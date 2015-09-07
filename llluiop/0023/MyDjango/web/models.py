from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age  = models.IntegerField()

    def __unicode__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
