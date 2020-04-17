from django import forms
from django.contrib.auth.models import User
from .models import Quiz, Questions
from django.utils.html import strip_tags

level_choice = (
        ("Undergraduate", "Undergraduate"),
        ("Advanced Higher","Advanced Higher"),
        ("Higher", "Higher"),
        ("National 5", "National 5"),
        ("National 4", "National 4"),
    )
    
subject_choice = (
        ("Computing", "Computing"),
        ("Geography","Geography"),
        ("History", "History"),
        ("Maths", "Maths"),
        ("French", "French"),
    )

class CreateQuizForm(forms.ModelForm):
    title = forms.CharField(label="Quiz Title", max_length=150)
    level = forms.ChoiceField(choices= level_choice)
    subject = forms.ChoiceField(choices= subject_choice)
    topic = forms.CharField(label="Topic", max_length = 30)

    #Cleans the user input and strips tags
    def clean_title(self):
        title = self.cleaned_data.get("title")
        banned_characters = [';',':','!','*','()','(',')','}','"',"'"]
        strip_title = strip_tags(title)
        new_title = ''.join(i for i in strip_title if not i in banned_characters)
        return new_title
    
    class Meta:
        model = Quiz
        fields = ['title','subject','level','topic']


class CreateQuestionForm(forms.ModelForm):
    question = forms.CharField(label = "Question:", max_length = 400)
    correct_answer = forms.CharField(label = "Correct Answer", max_length = 400)
    incorrect_answer_1 = forms.CharField(label = "Incorrect Answer 1: ", max_length = 400)
    incorrect_answer_2  = forms.CharField(label = "Incorrect Answer 2: ", max_length = 400)
    incorrect_answer_3  = forms.CharField(label = "Incorrect Answer 3: ", max_length = 400)
    incorrect_answer_4  = forms.CharField(label = "Incorrect Answer 4: ", max_length = 400)

    def clean_inputs(self):
        question = self.cleaned_data.get("question")
        correct_answer = self.cleaned_data.get("correct_answer")
        incorrect_answer_1 = self.cleaned_data.get("incorrect_answer_1")
        incorrect_answer_2 = self.cleaned_data.get("incorrect_answer_2")
        incorrect_answer_3 = self.cleaned_data.get("incorrect_answer_3")
        incorrect_answer_4 = self.cleaned_data.get("incorrect_answer_4")

        return question,correct_answer,incorrect_answer_1,incorrect_answer_2,incorrect_answer_3,incorrect_answer_4

    class Meta:
        model = Questions
        fields = ['question','correct_answer', 'incorrect_answer_1', 'incorrect_answer_2',
                  'incorrect_answer_3', 'incorrect_answer_4',]

    

    
    