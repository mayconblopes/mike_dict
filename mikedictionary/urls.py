from django.urls import path

from mikedictionary import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),

]