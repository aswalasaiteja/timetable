from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('credentials/', views.credentials, name = 'credentials'),
    path('add/',views.add, name = 'add')
]
