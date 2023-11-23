from django.contrib import admin
from apps.what_we_do.models import Projects, Editions, Reports
from parler.admin import TranslatableAdmin


@admin.register(Projects)
class ProjectsAdmin(TranslatableAdmin):
    list_display = ('name', 'description', 'attachment', 'order')
    list_editable = ('order',)


@admin.register(Reports)
class ReportsAdmin(TranslatableAdmin):
    list_display = ('name', 'attachment', 'order')
    list_editable = ('order',)


@admin.register(Editions)
class EditionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'writer', 'publisher')
