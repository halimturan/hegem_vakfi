from django.contrib import admin
from apps.site_settings.models import SocialMediaSettings, SiteSettings, Menu, MenuLocation
from parler.admin import TranslatableAdmin
from mptt.admin import MPTTModelAdmin


@admin.register(SocialMediaSettings)
class SocialMediaSettingsAdmin(admin.ModelAdmin):
    list_display = ('twitter', 'facebook', 'instagram', 'twitter')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address')


@admin.register(MenuLocation)
class MenuLocationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Menu)
class MenuAdmin(TranslatableAdmin):
    list_display = ('name', 'parent', 'menu_location', 'alignment')
    list_filter = ('menu_location',)
    list_editable = ['alignment', 'parent']
