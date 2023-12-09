from django.contrib import admin
from apps.announcements.models import Announcements
from parler.admin import TranslatableAdmin


@admin.register(Announcements)
class AnnouncementsAdmin(TranslatableAdmin):
    list_display = ('name', 'slug', 'order', 'is_publish')
    list_editable = ['is_publish', 'order']
