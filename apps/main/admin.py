from django.contrib import admin
from apps.main.models import MainSlider, Contact, Pages
from parler.admin import TranslatableAdmin
from django.utils.html import format_html


@admin.register(MainSlider)
class SocialMediaSettingsAdmin(TranslatableAdmin):
    list_display = ('name', 'order')
    list_editable = ['order', ]


@admin.register(Contact)
class ContactAdmin(TranslatableAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')


@admin.register(Pages)
class PagesAdmin(TranslatableAdmin):
    list_display = ('name', 'link_tr', 'link_en', 'created_by', 'updated_by', 'created_at')

    def link_tr(self, obj):
        return format_html(f'<a href="/tr/sayfalar/{obj.slug}">/tr/sayfa/{obj.slug}</a>')

    def link_en(self, obj):
        return format_html(f'<a href="/en/pages/{obj.slug}">/en/pages/{obj.slug}</a>')

    link_tr.allow_tags = True
    link_en.allow_tags = True