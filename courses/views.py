from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course, Lesson
from courses.forms import CreateCourseForm, CreateLessonForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

@login_required
def course_view(request):
    re = Course.SUBJECT_CHOICE

    args ={
        "subjects": re,
    }
    return render(request, 'courses/course_home.html', args)

@login_required
def create_course(request):
    user = request.user
    create_form = CreateCourseForm(request.POST)
    if request.method == "POST":
        print("hello")
        if create_form.is_valid():
            name = create_form.cleaned_data.get('name')
            description = create_form.cleaned_data.get('description')
            instance = create_form.save(commit=False)
            instance.name = name
            instance.description = description
            instance.user = user
            instance.save()
            return HttpResponseRedirect('/lesson-create')
   
    args  ={
        "form": create_form
    }

    return render(request, 'courses/course_create.html', args)

@login_required
def view_courses(request, subject):

    courses = Course.objects.filter(subject=subject)

    if courses:
        args  ={"all_courses": courses}
    else:
        args ={
        "all_courses": "There are currently no courses available for this subject!"}

    return render(request, 'courses/all_courses.html', args)



@login_required
def create_lesson(request):

    if request.method == "POST":
        form = CreateLessonForm(request.POST)
        args  = {
            "form": form
        }

    return render(request, 'courses/lesson_create.html', args)