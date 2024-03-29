from email import message
from django.shortcuts import redirect, render
from sympy import HomomorphismFailed
from . forms import *
from django.contrib import messages
from django.views import generic

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form = Notesform(request.POST)
        if form.is_valid():
            notes = Notes(user = request.user, title= request.POST['title'],description = request.POST['description'])
            notes.save()
        messages.success(request,f"Notes Added from {request.user.username} Successfully!") # messages hoito
    else:
        form = Notesform()        
    form = Notesform()
    notes = Notes.objects.filter(user=request.user) # notes is my model name
    context = {'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

# new function for delete notes
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

# new function for detail view
class NotesDetailView(generic.DetailView):
    model = Notes
    
    
# new function for homework section
def homework(request):
    
    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    context = {
            'homeworks':homework,
            'homework_done':homework_done,
             
    }
    return render(request,'dashboard/homework.html',context)





    

