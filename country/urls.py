from django.urls import path
from .views import search,index

urlpatterns = [
    path('search/', search,name='search'),
    path('', index, name='index'),
]
