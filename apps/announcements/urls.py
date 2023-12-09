from django.urls import path
from apps.announcements.views import *
from django.utils.translation import gettext_lazy as _

app_name = 'announcements'

urlpatterns = [
    path('', all_announcements, name='all_announcements'),
    path(_('detay/<str:announcements_slug>'), announcements_detail, name="announcements_detail")
]
