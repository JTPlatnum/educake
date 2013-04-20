from django.db import models
from django.contrib.auth.models import User

class Favorites(models.Model):
    user = models.ForeignKey(User)
    program_id = models.IntegerField()
    created_at = models.DateTimeField('date created at')
    updated_at = models.DateTimeField('date updated at')

