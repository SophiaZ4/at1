from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.TextField()

    def __str__(self):
        return self.question_text

#data of the two task types
class Task(models.Model):
    TASK_TYPES = (
        ('homework', 'Homework'),
        ('assessment', 'Assessment'),
    )

#model with each data set with restrictions
    task_name = models.CharField(max_length=15)
    task_type = models.CharField(max_length=10, choices=TASK_TYPES)
    subject = models.CharField(max_length=15)
    due_date = models.DateField()
    task_requirements = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name