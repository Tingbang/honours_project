from django.urls import path
from django.conf.urls import url, include
from courses import views

urlpatterns = [
    path('course-landing/', views.course_view, name='course-landing'),
    path('course-create/',views.create_course, name='course-create'),
    path('lesson-create/',views.create_lesson, name='lesson-create'),
    url(r'courses/(?P<subject>[\w|\W]+)/$', views.view_courses, name='view-courses')
]
