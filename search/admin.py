from django.contrib import admin
<<<<<<< HEAD
from search.models import Programs, Degree_Level, Degree_Subject, Schools

class Programs_Admin(admin.ModelAdmin):
    fields = ['school', 'degree_level', 'degree_subject', 'name', 'description', 'cost', 'link', 'created_at', 'updated_at']
admin.site.register(Programs, Programs_Admin)

class Degree_Level_Admin(admin.ModelAdmin):
    fields = ['name', 'created_at', 'updated_at']           
admin.site.register(Degree_Level, Degree_Level_Admin)

class Degree_Subject_Admin(admin.ModelAdmin):
    fields = ['name', 'created_at', 'updated_at']
admin.site.register(Degree_Subject, Degree_Subject_Admin)

class Schools_Admin(admin.ModelAdmin):
    fields = ['name', 'description', 'city', 'state', 'created_at', 'updated_at']
admin.site.register(Schools, Schools_Admin)
=======
from search.models import Schools, Degree_Level, Degree_Subject, Programs

admin.site.register(Schools)
admin.site.register(Degree_Level)
admin.site.register(Degree_Subject)
admin.site.register(Programs)
>>>>>>> f4a498fb0ad936ded03e14a7ac1047f24d30eb57
