from django.urls import path

from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    #path('registro/', views.PaginaRegistro, name="registro"),
	#path('login/', views.PaginaLogin, name="login"),  
	#path('logout/', views.logoutUser, name="logout"),
    path('', views.inicio, name="inicio"),
]