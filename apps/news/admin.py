from django.contrib import admin
from apps.news.models import News, Images
from parler.admin import TranslatableAdmin


@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = ('name', 'slug')


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('img',)
