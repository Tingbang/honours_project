from django.contrib import admin
from .models import Post

#Registers the blog app with the admin panel
admin.site.register(Post)