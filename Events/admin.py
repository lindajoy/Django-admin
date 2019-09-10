from django.contrib import admin
from .models import Epic,Event,EventHero,EventVillain
from django.contrib.admin import AdminSite

@admin.register(Epic)
class EpicAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(EventHero)
class EventHeroAdmin(admin.ModelAdmin):
    pass

@admin.register(EventVillain)
class EventVillainAdmin(admin.ModelAdmin):
    pass

class EventAdminSite(AdminSite):
    site_header = "Joy Events Admin"
    site_title = "Joy Admin Events Portal"
    index_title = "Welcome to events Researches Done By Joy"

event_admin_site = EventAdminSite(name ='event_admin')

event_admin_site.register(Epic)
event_admin_site.register(Event)
event_admin_site.register(EventHero)
event_admin_site.register(EventVillain)