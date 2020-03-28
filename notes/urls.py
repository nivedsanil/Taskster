from django.urls import path
from . import views 

urlpatterns = [

    path('addnote', views.addnote, name="addnote"),
    path('viewnote/<note_id>', views.viewnote, name="viewnote"), 
    path('delnote/<note_id>', views.delnote, name="delnote")
]