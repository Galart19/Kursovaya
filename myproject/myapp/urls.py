from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('load', views.load, name='load'),
    path('inference', views.inference, name='inference'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('news', views.news, name='news'),
]