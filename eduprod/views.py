from django.core import serializers
from django.shortcuts import render, redirect
from .models import Question
from .models import Task
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    tasks = Task.objects.order_by('due_date') #orders tasks by due date in a list on the home page
    return render(request, 'eduprod/home.html', {'tasks': tasks})

#function to add tasks with their respective task details
def add_task(request):
    if request.method == 'POST': #getting task details
        task_name = request.POST.get('task_name')
        task_type = request.POST.get('task_type')
        subject = request.POST.get('subject')
        due_date = request.POST.get('due_date')
        task_requirements = request.POST.get('task_requirements')

        if not task_type:
            return HttpResponseBadRequest("Task type is required") #error message if task type is not specified

        Task.objects.create( #adding to database with newly entered data
            task_name=task_name,
            task_type=task_type,
            subject=subject,
            due_date=due_date,
            task_requirements=task_requirements
        )
        return redirect('eduprod:home') #back to home page (where task list is displayed)
    return render(request, 'eduprod/add_task.html')

#function to mark tasks as complete
def mark_task_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = True #booleen update
    task.save()
    return redirect('eduprod:home')

#function to remove a task
def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('eduprod:home')