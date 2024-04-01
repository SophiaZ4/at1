from django.urls import path
from . import views

urlpatterns = [
    #path("", views.login_view, name="login"),
    path('home/', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'), #seperate website page for adding tasks
    path('mark_done/<int:task_id>', views.mark_task_done, name='mark_task_done'), #a page for marking specific tasks as done
    path('remove_task/<int:task_id>', views.remove_task, name='remove_task') #a page for deleting specific tasks
]

