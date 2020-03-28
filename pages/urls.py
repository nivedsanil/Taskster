from django.urls import path 
from . import views 

urlpatterns = [

    path('dashboard', views.dashboard, name="dashboard"),
    path('edittask/<task_id>', views.edittask, name="edittask")
]