from django.urls import path
from django.conf.urls import url, include
from courses import views

urlpatterns = [
    path('course-landing/', views.course_view, name='course-landing'),
    path('course-create/',views.create_course, name='course-create'),
    path('my-courses/',views.my_course, name='my-course'),
    url(r'modify-course/(?P<course_pk>\d+)/$', views.create_lesson, name='modify-course'),
    url(r'courses/(?P<subject>[\w|\W]+)/$', views.view_courses, name='view-courses'),
    url(r'course/(?P<course_pk>[\w|\W]+)/$', views.view_specific_course, name='view-this-course'),
    url(r'^publish/(?P<course_pk>\d+)/(?P<pub>[\w|\W]+)/$', views.publish_check, name="publish"),
    url(r'^delete/(?P<course_pk>\d+)/$', views.delete_course, name="delete-course")
   

    
]
