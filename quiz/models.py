from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Quiz -> (contains) Questions -> (Has Answers)
# Title, Subject, Level, Topic, Created By, Date Created
# 29/01/2020 - 
class Quiz(models.Model):
    title = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 20)
    level = models.CharField(max_length = 25)
    topic = models.CharField(max_length = 25)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    class Meta:
        verbose_name_plural = "quiz"

class Questions(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length = 350)
    correct_answer = models.CharField(max_length = 400)
    incorrect_answer_1 = models.CharField(max_length = 400, default ='')
    incorrect_answer_2 = models.CharField(max_length = 400, default ='')
    incorrect_answer_3 = models.CharField(max_length = 400, default ='')
    incorrect_answer_4 = models.CharField(max_length = 400, default ='')

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    class Meta:
        verbose_name_plural = "questions"

#incorrect answers
class Choice(models.Model):
    #foreign key to questions, this should include the users choice/correct/incorrect answers
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length = 300)
    incorrect_answers = models.CharField(max_length = 1000)
    correct = models.CharField(max_length = 3)
    
    class Meta:
        verbose_name_plural = "choices"


#Results Table
#Quiz name, user refrence, score for that particular quiz
#Could get all results taken for that quiz and find the average of all scores
#
