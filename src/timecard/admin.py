from django.contrib import admin
from timecard.models import Entry

class EntryAdmin(admin.ModelAdmin):
	list_display = ('date', 'user', 'start_time', 'end_time', 'hours', 'status', )
	list_filter = ('status', 'user',)
	date_hierarchy = 'date'

admin.site.register(Entry, EntryAdmin)