from django.contrib import admin
from .models import ItemModel

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'image')
    list_display_links = ('name', 'id')

admin.site.register(ItemModel, ItemModelAdmin)
