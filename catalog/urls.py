from django.urls import path

from .views import base, triangle_calculate

app_name = 'catalog'
urlpatterns = [
    path('', base, name="base"),
    path('catalog/', triangle_calculate, name='index'),
]
