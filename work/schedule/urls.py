from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('credentials/', views.credentials, name = 'credentials'),
    path('add-schedule/',views.add_schedule, name = 'add-schedule'),
    path('logout/', views.signout, name = 'logout'),
    path('delete-schedule/<int:id>', views.delete_schedule, name = 'delete-schedule' )
]
