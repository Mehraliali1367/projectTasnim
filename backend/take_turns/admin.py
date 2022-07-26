from django.contrib import admin
from . import models


# admin.site.register(models.Doctor)


@admin.register(models.Doctor)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')


@admin.register(models.Services)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('service',)


@admin.register(models.Presence)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'datetime_persian', 'from_hour', 'to_hour', 'interval_sick')


@admin.register(models.Visit)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'datetime_persian', 'hour', 'user')
