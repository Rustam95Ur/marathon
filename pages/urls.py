from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:page_slug>', views.page_view, name='page_view'),
]
