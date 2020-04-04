from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='blog-landing'),
    path('', views.home, name ='blog-home'),
    path('about/', views.about, name='blog-about'),
]

