from django import forms
from django.utils.html import strip_tags
from .models import Lesson, Course
from django_bleach.forms import BleachField

class CreateCourseForm(forms.ModelForm):
    name = forms.CharField(label="Course Title", max_length = 45)
    description = BleachField(label= "Course Description", max_length=2500)
    subject = forms.ChoiceField(choices= Course.SUBJECT_CHOICE)
    class Meta:
        model = Course
        fields = ['name','subject']

class CreateLessonForm(forms.ModelForm):
    all_the_content = BleachField(label="Course Content", max_length=1500)
    additional_content_1 = BleachField(label="additonal content 1", max_length=1500,required=False)
    additional_content_2 = BleachField(label="additonal content2", max_length=1500,required=False)
    file_upload = forms.FileField(required=False)
    file_upload_1 = forms.FileField(required=False)
    file_upload_2 = forms.FileField(required=False)
    file_upload_3 = forms.FileField(required=False)

    class Meta:
        model = Lesson
        fields = ['all_the_content','additional_content_1','additional_content_2','file_upload']



