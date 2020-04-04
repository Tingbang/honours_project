from django.urls import path
from django.conf.urls import url, include
from django.conf.urls import url, include
from . import views

urlpatterns =[
    path('statistics/', views.stats_home, name='stats-home'),
    path('get-stat/', views.stats_home_get, name='stats-get'),
    url(r'^get-quiz/(?P<quiz_check>[\w|\W]+)/$', views.get_previous_scores, name='get-previous')
    

]