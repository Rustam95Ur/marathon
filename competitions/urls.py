from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.competitions_list, name='competitions_list'),
    path('view/<int:competition_id>', views.competition_view, name='competition_view'),
    path('search/<int:competition_id>/<int:user_val>/', views.competition_search, name='competition_view'),


]