from django.contrib import admin
from . import models


@admin.register(models.Nas)
class NasAdmin(admin.ModelAdmin):
    list_display = ['nasname', 'type', 'ports']


@admin.register(models.RadAcct)
class RadAcctAdmin(admin.ModelAdmin):
    list_display = ['username', 'realm']


@admin.register(models.RadCheck)
class RadCheckAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'attribute', 'op', 'value']
    list_filter = ['attribute', 'op']
    search_fields = ['username']


@admin.register(models.RadGroupCheck)
class RadGroupCheckAdmin(admin.ModelAdmin):
    list_display = ['groupname']


@admin.register(models.RadGroupReply)
class RadGroupReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'groupname', 'attribute', 'op', 'value']


@admin.register(models.RadPostAuth)
class RadPostAuthAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'reply', 'authdate']
    list_filter = ['reply', 'authdate']
    search_fields = ['username']


@admin.register(models.RadReply)
class RadReplyAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(models.RadUserGroup)
class RadUserGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'groupname', 'priority']
    list_filter = ['groupname', 'priority']
    search_fields = ['username']
