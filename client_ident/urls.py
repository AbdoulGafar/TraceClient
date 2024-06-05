from django.urls import path
from .views import submit_client_info, success

urlpatterns = [
    path('', submit_client_info, name='submit_client_info'),
    path('success/', success, name='success'),
]
