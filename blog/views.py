from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def landing(request):
    return render(request, 'blog/landing.html')

def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def test(request):
    return render(requst, 'blog/test.html')