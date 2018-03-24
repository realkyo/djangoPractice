from django.contrib import admin
from recipe.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)