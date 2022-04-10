from django.urls import path
from .views import base_view, carusel_view

app_name = 'basepage'

urlpatterns = [
    path('', base_view, name='index'),
    path('carusel/', carusel_view, name='carusel'),
]