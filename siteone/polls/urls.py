from django.urls import path

from.import views

urlpatterns=[
    path("", views.index, name="index"),
]

# kiosk/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),
]
