from django.contrib import admin
from .models import *



class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Restaurants)
admin.site.register(Rubrics)
admin.site.register(Dishes, DishAdmin)
admin.site.register(MenuSections)
