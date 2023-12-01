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


DEFAULT_SEARCH_FIELDS = ['title__istartswith']


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    inlines = (VideoAdminInline, AudioAdminInline, TextAdminInline)
    search_fields = DEFAULT_SEARCH_FIELDS


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = DEFAULT_SEARCH_FIELDS


@admin.register(models.Audio)
class AudioAdmin(admin.ModelAdmin):
    search_fields = DEFAULT_SEARCH_FIELDS


@admin.register(models.Text)
class TextAdmin(admin.ModelAdmin):
    search_fields = DEFAULT_SEARCH_FIELDS
