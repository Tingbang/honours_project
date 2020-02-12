from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='blog-landing'),
    path('', views.home, name ='blog-home'),
    path('test/', views.home, name='blog-test'),
    path('about/', views.about, name='blog-about'),
]

