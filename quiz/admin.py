from django.contrib import admin

# Register your models here.
from .models import Quiz, Questions, Choice

admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Choice)