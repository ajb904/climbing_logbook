from django.contrib import admin

# Register your models here.

from logbook.models import *

class CragAdmin(admin.ModelAdmin):
	list_display = ('name', 'area', 'rock_type')
	search_fields = ('name', 'area', 'rock_type')

class SectorAdmin(admin.ModelAdmin):
	list_display = ('name', 'crag')
	list_filter = ('crag',)
#	date_hierarchy = 'publication_date'
#	ordering = ('-publication_date',)
#	filter_horizontal = ('authors',)

admin.site.register(Guidebook_area)
admin.site.register(Rock_type)
admin.site.register(Crag, CragAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Route)
admin.site.register(Partner)
admin.site.register(Log_entry)
admin.site.register(Grade_system)
