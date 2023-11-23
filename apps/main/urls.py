from django.urls import path
from apps.main.views import *
from django.utils.translation import gettext_lazy as _

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path(_('iletisim'), contact, name="contact"),
    path(_('sayfalar/<str:slug>'), pages, name="pages"),
]
