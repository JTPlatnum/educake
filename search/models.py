from django.db import models    

class Degree_Level(models.Model):
    name = models.CharField(max_length = 200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField() 

class Degree_Subject(models.Model):
    name = models.CharField(max_length = 200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField() 

class Schools(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    location = models.CharField(max_length = 200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
class Programs(models.Model):
    school = models.ForeignKey(Schools)
    degree_subject = models.ForeignKey(Degree_Subject)
    degree_level = models.ForeignKey(Degree_Level)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    cost = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()