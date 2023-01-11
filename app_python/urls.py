from django.urls import path

from .views import login, logout, signup

urlpatterns = [
    path('login', login, name='login'),
    path('deconnexion/', logout, name='logout'),
    path('inscription/', signup(), name='signup'),
]
