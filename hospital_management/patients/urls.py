from django.contrib import admin
from django.urls import path

# from patients import views
from . import views

urlpatterns = [
    path('',views.setcookie,name='setcookie'),
    path('main', views.Base.as_view(), name='main'),
    path('book',views.Main.as_view(),name='book'),

]