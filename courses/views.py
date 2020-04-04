from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course, Lesson
from courses.forms import CreateCourseForm, CreateLessonForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

@login_required
def course_view(request):
    re = Course.SUBJECT_CHOICE
    user_name = request.user

    my_courses = Course.objects.filter(user=user_name)
    args ={
        "subjects": re,
        "my_published": my_courses
    }
    return render(request, 'courses/course_home.html', args)

@login_required
def my_course(request):
    user = request.user
    all_my_course = Course.objects.filter(user=user)
    args ={
        "my_courses": all_my_course
    }

    return render(request, 'courses/my_courses.html', args)

@login_required
def view_specific_course(request, course_pk):
    get_all_lessons = Lesson.objects.filter(course=course_pk)

    args ={
        "all_lessons": get_all_lessons
    }


    return render(request, 'courses/course_view.html', args)

@login_required
def create_course(request):

    user = request.user
    create_form = CreateCourseForm(request.POST)
    if request.method == "POST":
        print("hello")
        if create_form.is_valid():
            name = create_form.cleaned_data.get('name')
            description = create_form.cleaned_data.get('description')
            subject = create_form.cleaned_data.get('subject')
            instance = create_form.save(commit=False)
            instance.name = name
            instance.description = description
            instance.subject = subject
            instance.user = user
            instance.slug = (subject + "-Course")
            instance.save()
            # pk_session = Course.objects.filter(name=name).values_list('id', flat=True)
            # print(pk_session)
            # pk_set = str(pk_session)

            # request.session['course_session'] = pk_set
            return HttpResponseRedirect('/my-courses')
   
    args  ={
        "form": create_form
    }

    return render(request, 'courses/course_create.html', args)

@login_required
def view_courses(request, subject):

    courses = Course.objects.filter(subject=subject)
 
    args  ={"all_courses": courses,
            "subject": subject}

    return render(request, 'courses/all_courses.html', args)

@login_required
def create_lesson(request, course_pk):
    session = request.session.get('course_session')
    form = CreateLessonForm(request.POST)
    pk = Course.objects.filter(pk=course_pk).first()
    count = Lesson.objects.filter(course=pk).count()
    count= count+1
    print(count)
    args  = { "form": form,
              "Course": pk,
              "lesson_count": count }

    if request.method == "POST":
        if form.is_valid():

            course = session
            all_the_content= form.cleaned_data.get('all_the_content')
            additional_1 = form.cleaned_data.get('additional_content_1')
            additional_2 =form.cleaned_data.get('additional_content_2')
            instance = form.save(commit=False)
            instance.course = pk
            instance.all_the_content = all_the_content
            instance.additional_content_1 = additional_1
            instance.additional_content_2 = additional_2
            instance.file_upload = form.cleaned_data.get('file_upload')
            instance.lesson = count
            instance.save()
            #del request.session['course_session']
            return HttpResponseRedirect('/modify-course')


    return render(request, 'courses/lesson_create.html', args)

@login_required
def publish_check(request, course_pk, pub):
    checked = pub
    course = Course.objects.get(id=course_pk)
    course.published = pub
    course.save()
    return HttpResponseRedirect('/my-courses')


@login_required
def delete_course(request, course_pk):
    course = Course.objects.filter(id=course_pk).delete()

    return HttpResponseRedirect('/my-courses')
        

    

