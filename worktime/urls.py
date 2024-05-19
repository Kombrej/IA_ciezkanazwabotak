from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='templates/WorkTime/base.html'),
    path('home', views.home, name='templates/WorkTime/home.html'),
]
