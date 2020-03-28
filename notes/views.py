from django.shortcuts import render, redirect
from . models import Note
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/')
def addnote(request):

    if request.method == 'POST':
        
        username = request.user
        title=request.POST['title']
        description=request.POST['description']


    note=Note(title=title, description=description, username=username)
    note.save()

    return redirect('/pages/dashboard')

@login_required(login_url='/')
def viewnote(request, note_id):

    viewnote=Note.objects.get(id=note_id)

    context={

        'viewnote':viewnote
    }
    return render(request, "pages/notepad.html", context)

@login_required(login_url='/')
def delnote(request, note_id):

    note_to_delete=Note.objects.get(id=note_id)
    note_to_delete.delete()
    return redirect('/pages/dashboard')


