from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

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
    weighting = models.IntegerField(default = 1)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return self.quiz.get_absolute_url()
        
    class Meta:
        verbose_name_plural = "questions"

#incorrect answers
#take quiz, present results on front end using jquery, then store in back end to be later viewed in statistics
class Choice(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length = 300)
    user_answer = models.CharField(max_length = 1000)
    #correct = models.BoolField(default = false)
    
    class Meta:
        verbose_name_plural = "choices"


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Quiz:{} - {}'.format(self.quiz,self.user)
    
    class meta:
        verbose_name_plural="result"
