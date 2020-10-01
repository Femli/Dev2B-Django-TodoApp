from django.urls import path
from . import views ## in this same folder, we are importing the objects in views.py

urlpatterns = [
    # URL Pattern: /home/
    path('', views.index, name='home'),
    
    # URL Pattern: /home/#/
    path('<int:bagel_id>/', views.bagels, name='bagels'),
    
    # URL Pattern: /home/#/results/
    path('lore/<str:name>/', views.lore, name='lore'),
]