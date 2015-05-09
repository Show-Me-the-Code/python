from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length = 20)
    context = models.CharField(max_length = 200)
    vote_date = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.context
    
