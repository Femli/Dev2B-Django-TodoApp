from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

## The functions below will provide specific view to our application


# this is taking in the information about our tasks, given by the model file
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}

    return render(request, 'list/services.html', context)

def updateTask(request, pk): #'pk' is going to be the 'primary key', which is the row id in the database, of our tasks.
    task = Task.objects.get(id=pk) # We will use this to order our tasks, and make the url route dynamic to each task

    form = TaskForm(instance=task) #the 'instance=task' allows us to pre-fill a form with our task attributes

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) # we don't want to create a new form, but rather use the already populated form with our task attributes
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'list/update.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk) # this will allow us to pass the title of our task, so we can confirm it's deletion

    if request.method == "POST":
        item.delete() # this will remove the task from our database
        return redirect('/')

    context = {'item':item}
    return render(request, 'list/delete.html', context)