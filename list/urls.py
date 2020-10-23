from django.urls import path
from . import views ## in this same folder, we are importing the objects in views.py

urlpatterns = [
    path('', views.hotdog, name='hotdog'), ## views.index is the name of the function housing our http request
    path('<int:menu_id>/', views.choice, name='choice'),
    path('hello/', views.hello, name="hello"),
    path('home/', views.home, name="home"),
    path('contact-us/', views.contactus, name="contact-us"),
    path('services/', views.services, name='services'),
    path('child/', views.child, name="child")
]