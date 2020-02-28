from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateQuizForm
from quiz.forms import CreateQuizForm
from quiz.forms import CreateQuestionForm
from quiz.models import Quiz, Questions
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import strip_tags
from django.core import serializers
import json
from django.http import JsonResponse

@login_required
def create_quiz(request):
    user = request.user
    form = CreateQuizForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data.get('title')
            topic = form.cleaned_data.get('topic')
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/my_quiz')
        else:
            form = CreateQuizForm()
    return render(request, 'quiz/create_form.html', {'form':form})

@login_required
def create_questions(request):
    user = request.user
    form = CreateQuestionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            newquiz = quiz
            question = form.cleaned_data.get('correct_answer')
            correct_answer = form.cleaned_data.get('correct_answer')
            incorrect_answer_1 = form.cleaned_data.get('incorrect_answer_1')
            incorrect_answer_2  = form.cleaned_data.get('incorrect_answer_2')
            incorrect_answer_3  = form.cleaned_data.get('incorrect_answer_3')
            incorrect_answer_4  = form.cleaned_data.get('incorrect_answer_4')
            instance = form.save(commit=False)
            instance.quiz = newquiz
            instance.save()
            
            return HttpResponseRedirect('/my_quiz')

    else:
        #Re-Render
        form = CreateQuestionForm()
    return render(request, 'quiz/create_questions.html', {'form': form})

#Make sure to pass the user to ensure that only the author of the quiz can view******
#When a user clicks "edit", take them to a page that retrieves that specific quizzes details
#To be able to add questions and answers
#** QUESTION MARK WEIGHTING
@login_required
def view_my_quiz(request, pk=None, auth=None, quz=None):
    form = CreateQuestionForm(request.POST)
    user = request.user
    user_check = str(request.user)

    if request.is_ajax():
        if form.is_valid():
            quiz = Quiz.objects.filter(pk=pk).first()
            question = form.cleaned_data.get('question')
            correct_answer = form.cleaned_data.get('correct_answer')
            incorrect_answer_1 = form.cleaned_data.get('incorrect_answer_1')
            incorrect_answer_2  = form.cleaned_data.get('incorrect_answer_2')
            incorrect_answer_3  = form.cleaned_data.get('incorrect_answer_3')
            incorrect_answer_4  = form.cleaned_data.get('incorrect_answer_4')

            response_data ={}

            response_data['question'] = question

            instance = form.save(commit=False)
            instance.quiz = quiz
            instance.save()
           
            return HttpResponse(json.dumps(response_data), content_type="application/json")            

    if pk and (user_check == auth):
        my_quiz = Quiz.objects.filter(pk=pk, author=user)
        questions = Questions.objects.filter(quiz=pk)
        args = {'quiz': my_quiz, 'question': questions, 'title': quz, 'form': form}
    else:
        return HttpResponseRedirect('/my_quiz')
    
    return render(request, 'quiz/modify_quiz.html', args)


@login_required
def quiz_home(request):
    all_Q = Quiz.objects.all()

    args = {'quiz': all_Q}


    return render(request, 'quiz/take_quiz_menu.html', args)

@login_required
def get_questions(request):
    quiz_session = request.session.get('quiz_session')
    if request.is_ajax():
        if request.method =="GET":
            serial = serializers.serialize("json", Questions.objects.filter(quiz=quiz_session))
            response_data = serial
            del request.session['quiz_session']
            return HttpResponse(response_data, content_type="application/json")


@login_required
def active_quiz(request, quiz_pk):
    quiz = Quiz.objects.filter(pk=quiz_pk)
    questions = Questions.objects.filter(quiz=quiz_pk)
    request.session['quiz_session'] = quiz_pk

    args={'question': questions, 'quiz': quiz}
    return render(request, 'quiz/quiz_active.html', args)
    