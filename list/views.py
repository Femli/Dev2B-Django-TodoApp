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