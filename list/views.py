from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

## The functions below will provide specific view to our application


## Example 1 - hello word with the current time
def index(request): ## keep the name of this view function in mind, as it will be imported in another file 
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return HttpResponse("Hello World! \n The current time is: %s" % (current_time))