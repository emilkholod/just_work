from django.contrib import admin

from . import models


class VideoAdminInline(admin.StackedInline):
    model = models.Video
    extra = 1


class AudioAdminInline(admin.StackedInline):
    model = models.Audio
    extra = 1


class TextAdminInline(admin.StackedInline):
    model = models.Text
    extra = 1


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    inlines = (VideoAdminInline, AudioAdminInline, TextAdminInline)
    search_fields = ['title__istartswith']
