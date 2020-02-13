from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns =[
    path('quiz/', views.quiz_home, name='quiz-home'),
    path('create_quiz/', views.create_quiz, name='quiz-create'),
    path('create_question/', views.create_questions, name='question-create'),
    url(r'^view-quiz/(?P<pk>\d+)/(?P<auth>[\w\-]+)/(?P<quz>[\w|\W]+)/$', views.view_my_quiz, name ='view-quiz'),
    path('take-quiz', views.quiz_home, name="take-quiz")
    
]