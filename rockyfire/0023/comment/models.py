from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    # name=models.ForeignKey(User,related_name="comment_user")
    name=models.CharField(max_length=80)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('created',)