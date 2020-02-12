from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Quiz, Questions
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def my_quiz(request):
     user = request.user
     user_posts = Quiz.objects.filter(author=request.user)
     user_questions = Questions.objects.filter
     args = {'posts': user_posts, 'questions': user_questions}
     return render(request, 'dashboard/my_quiz.html', args)
