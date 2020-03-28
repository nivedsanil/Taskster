from django.urls import path 
from . import views 

urlpatterns = [

    path('addtask', views.addtask, name="addtask"),
    path('deltask/<task_id>', views.deltask, name="deltask"),
    path('comptask/<task_id>', views.comptask, name="comptask"),
]