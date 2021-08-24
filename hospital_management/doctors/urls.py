from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('login', views.user_login, name='login'),
    path('appt', views.Appointment.as_view(), name='appt'),
    path('email/<int:id>', views.update.as_view(), name='confirm'),
    path('email',views.DisplayEmail, name='mailed'),
    path('log_out',views.log_out,name='logout')
]