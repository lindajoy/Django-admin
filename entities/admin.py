from django.contrib import admin
from .models import Hero, Villain, Category, Origin, HeroProxy, AllEntity, HeroAcquaintance
from django.contrib.admin import AdminSite
from django.db.models import Count
from django.shortcuts import render,redirect

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "is_immortal", "category", "origin", "is_very_benevolent")
    list_filter = ("is_immortal", "category", "origin",)

    def is_very_benevolent(self,obj):
        return obj.benevolence_factor>75

@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display =("name",'hero_count','villain_count')

    def get_queryset(self,request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _hero_count = Count('hero',distinct=True),
            _villain_count = Count('villain',distinct=True),

        )
        return queryset

    def hero_count(self, obj):
        return obj.hero_set.count()
    def villain_count(self, obj):
        return obj.villain_set.count()   

@admin.register(HeroProxy)
class HeroProxyAdmin(admin.ModelAdmin):
    pass

@admin.register(AllEntity)
class AllEntityAdmin(admin.ModelAdmin):
    pass

@admin.register(HeroAcquaintance)
class HeroAcquaintanceAdmin(admin.ModelAdmin):
    pass

from django.contrib.auth.models import User, Group
admin.site.unregister(User)
admin.site.unregister(Group)