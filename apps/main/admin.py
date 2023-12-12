from django.contrib import admin
from apps.main.models import MainSlider, Contact, Pages
from parler.admin import TranslatableAdmin
from django.utils.html import format_html
from django import forms


@admin.register(MainSlider)
class MainSliderAdmin(TranslatableAdmin):
    list_display = ('name', 'order', 'is_publish')
    list_editable = ['order', 'is_publish']


class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = '__all__'
        model = Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    form = ContactForm


@admin.register(Pages)
class PagesAdmin(TranslatableAdmin):
    list_display = ('name', 'link_tr', 'link_en', 'created_by', 'updated_by', 'created_at', 'updated_at', 'is_publish')
    list_editable = ['is_publish', ]

    def link_tr(self, obj):
        return format_html(f'<a href="/tr/sayfalar/{obj.slug}">/tr/sayfa/{obj.slug}</a>')

    def link_en(self, obj):
        return format_html(f'<a href="/en/pages/{obj.slug}">/en/pages/{obj.slug}</a>')

    link_tr.allow_tags = True
    link_en.allow_tags = True
