from django.db import models

class Favorites(models.Model):
    user_id = models.ForeignKey(Users)
    program_id = models.ForeignKey(degree_subject)
    created_at = models.DateTimeField('date created at')

