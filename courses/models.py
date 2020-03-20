from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# The Application has Courses. Courses are made up of one or more Lessons
class Course(models.Model):
    SUBJECT_CHOICE = (
                      ("Computing", "Computing"),
                      ("English", "English"),
                      ("Geography", "Geography"),
                      ("Chemistry", "Chemistry"),
                      ("Physics", "Physics"),
                      ("Music", "Music"),
                      ("Art", "Art"),
                      ("History", "History"), 
                    )

    name = models.CharField(max_length = 45)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    description = models.CharField(max_length=250)
    subject = models.CharField(max_length=15, choices=SUBJECT_CHOICE,default="Computing")
    slug = models.SlugField(default=name)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return self.course.get_absolute_url()

    class Meta:
        verbose_name_plural = "Course"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.IntegerField(default=1)
    all_the_content = models.CharField(max_length=1500)
    additional_content_1 = models.CharField(max_length=1500, blank=True, default='')
    additional_content_2 = models.CharField(max_length=1500, blank=True, default='')
    file_upload = models.FileField(null=True, blank=True)

