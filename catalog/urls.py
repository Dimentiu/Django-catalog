from catalog.views import base, new_person, select, triangle_calculate, update

from django.urls import path

app_name = 'catalog'
urlpatterns = [
    path('', base, name="base"),
    path('catalog/', triangle_calculate, name='index'),
    path('person/', new_person, name="new_person"),
    path('person/<int:pk>/', update, name="update"),
    path('person/select/', select, name='select')
]
