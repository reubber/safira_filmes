from django.contrib import admin
from .models import Filme
# Register your models here.

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year', 'description')
    list_filter = ('title', 'year')
    search_fields = ('title', 'genre', 'description')

admin.site.register(Filme, FilmeAdmin)