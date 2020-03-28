from django.shortcuts import render, redirect
from . models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def addtask(request):

    if request.method == 'POST':
        
        username = request.user
        title=request.POST['title']
        description=request.POST['description']


    task=Task(title=title, description=description, username=username)
    task.save()

    return redirect('/pages/dashboard')

@login_required(login_url='/')
def deltask(request, task_id):

    post_to_delete=Task.objects.get(id=task_id)
    post_to_delete.delete()
    return redirect('/pages/dashboard')


@login_required(login_url='/')
def comptask(request, task_id):

    post_to_complete=Task.objects.get(id=task_id)
    post_to_complete.is_completed=True
    post_to_complete.save()
    
    return redirect('/pages/dashboard')



        


