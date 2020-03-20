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

    quiz_filter = Result.objects.filter(quiz__title__contains="Test Quiz").aggregate(score=Avg('score'))

    #Works, got my desired results
    test1 = Result.objects.values('quiz__title').order_by('quiz').filter(user=user).annotate(scores=Avg('score')).distinct()
    print(test1[0]['scores'])

    avg = Result.objects.all().aggregate(Avg('score'))
    
    stat_data = Result.objects.filter(user=user)

    for choice in stat_data:
        choice_label.append(choice.quiz.title)
        choice_data.append(choice.score)

    args = {
        'quiz_filter': quiz_filter,
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
def stats_home_get(request):
    labels = []
    data = []
    user = request.user
    serial = serializers.serialize("json", Result.objects.filter(user=user))

    return HttpResponse(serial, content_type="application/json")

