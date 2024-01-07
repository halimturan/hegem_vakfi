from django.urls import path
from apps.payment.views import *

app_name = 'payment'

urlpatterns = [
    path('', make_payment, name='make_payment'),
    path('success', success_process, name="success_process"),
    path('fail', fail_process, name="fail_process"),
]
