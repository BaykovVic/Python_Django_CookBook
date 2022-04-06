from django.urls import path
from .views import base_view

app_name = 'basepage'

urlpatterns = [
    path('', base_view, name='index')
]