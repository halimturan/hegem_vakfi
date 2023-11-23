from django.urls import path
from apps.what_we_do.views import *
from django.utils.translation import gettext_lazy as _

app_name = 'what_we_do'

urlpatterns = [
    path(_('yayinlarimiz'), editions, name='editions'),
    path(_('projelerimiz'), projects, name='projects'),
    path(_('raporlarimiz'), reports, name='reports'),
]
