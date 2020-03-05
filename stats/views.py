from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Sum
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

    avg = Result.objects.all().aggregate(Avg('score'))
    print(avg)


    stat_data = Result.objects.filter(user=user)

    for choice in stat_data:
        choice_label.append(choice.quiz.title)
        choice_data.append(choice.score)

    args = {
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

