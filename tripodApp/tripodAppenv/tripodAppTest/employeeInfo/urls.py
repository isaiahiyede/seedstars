from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('add', views.add_user, name='add_user'),
    path('list', views.list_users, name='list_users'),
]