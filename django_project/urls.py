from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from quiz import views as quiz_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('register/', user_views.register, name ='register'),
    url('', include('dashboard.urls')),
    url('quiz', include('quiz.urls')),
    url('profile/', user_views.profile, name ='profile'),
    url('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name ='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name ='logout'),
    url('', include('blog.urls')),
    url('', include('quiz.urls')),
    
] 



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
