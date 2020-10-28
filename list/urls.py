from django.urls import path
from . import views ## in this same folder, we are importing the objects in views.py

urlpatterns = [
    path('', views.index, name='tasks'),
]