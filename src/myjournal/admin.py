from django.contrib import admin
from .models import JournalEntry

class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created_at')
    list_display_links = ('title', 'id')

admin.site.register(JournalEntry, JournalEntryAdmin)
