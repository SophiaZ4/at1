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

#restrictions for each data type
    task_name = models.CharField(max_length=100)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    subject = models.CharField(max_length=50)
    due_date = models.DateField()
    task_requirements = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name