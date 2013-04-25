from django.db import models    

class Degree_Level(models.Model):
    name = models.CharField(max_length = 200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField() 
    def __unicode__(self):
          return "name: %s, id: %d" %(self.name, self.id)    

class Degree_Subject(models.Model):
    name = models.CharField(max_length = 200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField() 
    def __unicode__(self):
          return "subject: %s, id: %d" %(self.name, self.id)  

class Schools(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    def __unicode__(self):
        return "school: %s, city: %s, state: %s, id: %d" %(self.name, self.city, self.state, self.id)      
    
class Programs(models.Model):
    school = models.ForeignKey(Schools)
    degree_level = models.ForeignKey(Degree_Level)
    degree_subject = models.ForeignKey(Degree_Subject)
    degree_level = models.ForeignKey(Degree_Level)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    cost = models.IntegerField()
    link = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    def __unicode__(self):
        return "school: %s, deg level: %s, deg subject: %s, name: %s, descript: %s, cost: %d, id: %d" %(self.school, self.degree_level, self.degree_subject, self.name, self.description, self.cost, self.id)     
