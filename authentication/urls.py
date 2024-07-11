# authentication/urls.py

from django.urls import path
from .views import sign_up, log_in, dashboard
from .views import log_out

urlpatterns = [
    path('', sign_up, name='sign_up'),
    path('log_in/', log_in, name='log_in'),
    path('dashboard/', dashboard, name='dashboard'),
    path('log_out/', log_out, name='log_out'),
]

