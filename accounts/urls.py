from django.urls import path 
from . import views 
from django.views.generic import TemplateView

urlpatterns = [

    path('', views.signin, name="signin"),
    # path('signup', TemplateView.as_view(template_name="register/signup.html"), name="signup"),
    path('signup', views.signup, name="signup"), 
    path('logout', views.logout, name="logout")
   
    
]