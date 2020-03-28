from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from tasks.models import Task
from notes.models import Note
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

@login_required(login_url='/')
def dashboard(request):

    currentuser=request.user
    task=Task.objects.filter(username=currentuser).filter(is_completed=False)
    comptask=Task.objects.filter(username=currentuser).filter(is_completed=True)
    note=Note.objects.filter(username=currentuser)


    context={
        'task':task,
        'comptask':comptask, 
        'note':note
    }

    return render(request, "pages/dashboard.html", context)

@login_required(login_url='/')

def edittask(request, task_id):

    edittask=Task.objects.get(id=task_id)

    if request.is_ajax():
        data = serializers.serialize('json', edittask)
        return HttpResponse(data,'json')

    else:

        return render(request, 'pages/dashboard.html', {'edittask':edittask})
    




