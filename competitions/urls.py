from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.competitions_list, name='competitions_list'),

]