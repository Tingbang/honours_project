from django.urls import path
from . import views

urlpatterns =[
    path('dashboard/', views.dashboard, name='dashboard-home' ),
    path('my_quiz/', views.my_quiz, name='dashboard-my_quiz' ),
]