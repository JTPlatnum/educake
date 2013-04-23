from django.contrib import admin
from search.models import Programs, Degree_Level, Degree_Subject, Schools

class Programs_Admin(admin.ModelAdmin):
    fields = ['school', 'degree_level', 'degree_subject', 'name', 'description', 'cost', 'created_at', 'updated_at']
admin.site.register(Programs, Programs_Admin)

class Degree_Level_Admin(admin.ModelAdmin):
    fields = ['name', 'created_at', 'updated_at']           
admin.site.register(Degree_Level, Degree_Level_Admin)

class Degree_Subject_Admin(admin.ModelAdmin):
    fields = ['name', 'created_at', 'updated_at']
admin.site.register(Degree_Subject, Degree_Subject_Admin)

class Schools_Admin(admin.ModelAdmin):
    fields = ['name', 'description', 'location', 'created_at', 'updated_at']
admin.site.register(Schools, Schools_Admin)