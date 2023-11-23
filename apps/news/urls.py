from django.urls import path
from apps.news.views import *
from django.utils.translation import gettext_lazy as _

app_name = 'news'

urlpatterns = [
    path('', all_news, name='all_news'),
    path(_('detay/<str:news_slug>'), news_detail, name="news_detail")
]
