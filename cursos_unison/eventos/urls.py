from django.urls import path

from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [

    path('', views.home, name="inicio"),
    path('registro/',views.registro,name='registro'),
    path('login/',views.loginPag,name='login'),
    path('logout/',views.logoutUsuario,name='logout'),

    path('ver_perfil/',views.verPerfil,name='ver_perfil'),
    path('editar_perfil/',views.editarPerfil,name='editar_perfil'),

    # ------------------- EVENTOS FORMATIVOS -------------
    path('PropuestasEventosFormativos/',views.PropuestasEventosFormativos, name="PropuestasEventosFormativos"),
    path('ver_propuesta/<str:pk>/', views.Propuesta, name="Propuesta"),
    path('editar_propuesta/<str:pk>', views.updatePropuesta, name="updatePropuesta"),
    path('crear_propuesta/<str:pk>/', views.createPropuesta, name="createPropuesta"),
    path('borrar_propuesta/<str:pk>/', views.deletePropuesta, name="deletePropuesta"),
]