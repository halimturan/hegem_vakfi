from django.urls import path
from apps.payment.views import *

app_name = 'payment'

urlpatterns = [
    path('', make_payment, name='make_payment'),
]
