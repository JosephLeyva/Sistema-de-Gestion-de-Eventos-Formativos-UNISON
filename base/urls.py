from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    

    path('home/', views.Home, name='home'),
    path('PropuestasEventosFormativos',views.PropuestasEventosFormativos, name="PropuestasEventosFormativos"),
    path('propuesta/<str:pk>/', views.Propuesta, name="Propuesta"),

    path('crear-propuesta/', views.createPropuesta, name="createPropuesta"),
    path('editar-propuesta/<str:pk>', views.updatePropuesta, name="updatePropuesta"),
    path('borrar-propuesta/<str:pk>', views.deletePropuesta, name="deletePropuesta"),
   
]
