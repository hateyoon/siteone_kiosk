from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, world. You're at the polls index.")

# kiosk/views.py
from django.shortcuts import render
from .models import Menu

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'kiosk/menu_list.html', {'menus': menus})
