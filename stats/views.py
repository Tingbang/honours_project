from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Sum, Max, Min
from quiz.models import Quiz, Questions, Result
from django.core import serializers
import random
from django.http import HttpResponse, HttpResponseRedirect

@login_required
def stats_home(request):
    user = request.user
    labels = []
    data = []
    choice_label = []
    choice_data = []
    serial = serializers.serialize("json", Result.objects.filter(user=user))
    quiz = Result.objects.filter(user=user)

    quiz_filter = Result.objects.values('score').filter(quiz__title__contains="Test Quiz")
    print(quiz_filter)

    available_quiz = Result.objects.values('quiz__title').filter(user=user).distinct()
    #print(available_quiz)


    #Works, got my desired results
    test1 = Result.objects.values('quiz__title').order_by('quiz').filter(user=user).annotate(scores=Avg('score')).distinct()

    avg = Result.objects.all().aggregate(Avg('score'))
    
    stat_data = Result.objects.filter(user=user)
    #print(stat_data)

    for choice in stat_data:
        choice_label.append(choice.quiz.title)
        choice_data.append(choice.score)

    args = {
        'quiz_filter': quiz_filter,
        'available_quiz': available_quiz,
        'test1': test1,
        'results': serial,
        'labels': labels,
        'average': avg,
        'data': quiz,
        'choice_label': choice_label,
        'choice_data': choice_data,
        'choice_colours': ['rgba(252, 186, 3'] * len(choice_data), 
    }

    
    return render(request, 'stats/home.html', args)


@login_required
def get_previous_scores(request, quiz_check):
    quiz_check = request.GET['quiz_check']
    query = Result.objects.filter(quiz__title__contains=quiz_check)
    serial = serializers.serialize("json", query, fields=('score','timestamp'))
    print(query)
    args ={
        "result": serial
    }

    return HttpResponse(serial, content_type="application/json")


@login_required
def stats_home_get(request):
    labels = []
    data = []
    user = request.user
    serial = serializers.serialize("json", Result.objects.filter(user=user))

    return HttpResponse(serial, content_type="application/json")

