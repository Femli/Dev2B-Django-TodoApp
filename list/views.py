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

def updateTask(request, pk): # 'pk' is going to be the primary key, which is the row id in the database, of our tasks
    task = Task.objects.get(id=pk) # we will use this to order our tasks, and make the url routing dynamic

    form = TaskForm(instance=task) # use a pre-populated form with the task info from our database

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) # use a pre-populated form with the task info from our database
        if form.is_valid():
            form.save()
        return redirect('/') # return back home :)

    context = {'form': form}
    return render(request, 'list/update.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete() # this will remove the task from our database
        return redirect('/')
        
    context = {'item': item}
    return render(request, 'list/delete.html', context)