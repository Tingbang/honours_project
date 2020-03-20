from django import forms
from django.utils.html import strip_tags
from .models import Lesson, Course
from django_bleach.forms import BleachField

class CreateCourseForm(forms.ModelForm):
    name = forms.CharField(label="Course Title", max_length = 45)
    description = BleachField(label= "Course Description", max_length=2500)
    subject = forms.ChoiceField(choices= Course.SUBJECT_CHOICE)

    #Cleans the user input and strips tags
    # def clean_title(self):
    #     title = self.cleaned_data.get("title")
    #     banned_characters = [';',':','!','*','()','(',')','}','"',"'"]
    #     strip_title = strip_tags(title)
    #     new_title = ''.join(i for i in strip_title if not i in banned_characters)
    #     return new_title
    

    class Meta:
        model = Course
        fields = ['name','subject']



class CreateLessonForm(forms.ModelForm):
    lesson = forms.IntegerField(max_value=30)
    all_the_content = BleachField(label="Course Content", max_length=2500)



    class Meta:
        model = Lesson
        fields = ['lesson', 'all_the_content']



