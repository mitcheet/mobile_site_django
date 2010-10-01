from librware.librware_mobile.models import Library, Hours, Contact, Location, Feed, ExternalLinks
from django.contrib import admin

class HoursInline(admin.TabularInline):
	model = Hours
class ContactsInLine(admin.TabularInline):
	model = Contact
	
class FeedInLine(admin.TabularInline):
	model=Feed

class LocationInLine(admin.TabularInline):
	model = Location 

class ExternalLinksInLine(admin.TabularInline):
	model = ExternalLinks

class LibraryAdmin(admin.ModelAdmin):
	inlines = [HoursInline, ContactsInLine, FeedInLine, LocationInLine, ExternalLinksInLine]
	list_filter = ['libraryName']
	search_fields = ['libraryName']
admin.site.register(Library, LibraryAdmin)
#admin.site.register(Contact)
#admin.site.register(Hours)
#admin.site.register(Location)
