from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('register/', views.reg, name='Register'),
    path('registerw/', views.workerreg, name='RegisterW'),
    path('login/', views.log, name='login'),
    path('logout/', views.logout, name='logout'),
]
