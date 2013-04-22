from django.contrib import admin
from favorites.models import Favorites

#admin.site.register(Favorites)

class FavoritesAdmin(admin.ModelAdmin):
    fields = ['user', 'program_id', 'created_at', 'updated_at']
              
admin.site.register(Favorites, FavoritesAdmin)