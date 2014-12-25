from django.db import models


class Messages(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    content = models.CharField(max_length=300)