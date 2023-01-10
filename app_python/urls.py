from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('deconnexion/', views.logout, name='logout'),
    path('inscription/', views.register, name='register'),
]
