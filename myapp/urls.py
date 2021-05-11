
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = "index-page"),
    path('contact/', views.contact,name = "contactus"),
    path('send-courier/', views.send_courier,name = "send-courier"),
    path('about/', views.about,name = "about-page"),
    path('track/', views.track,name = "track-page"),
    path('login/', views.login,name = "login-page"),  

]
