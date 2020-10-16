from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

## The functions below will provide specific view to our application


## Example 1 - hello word with the current time
def index(request): ## keep the name of this view function in mind, as it will be imported in another file 
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return HttpResponse("Hello World! \n The current time is: %s" % (current_time))

def potatoes(request):
    return HttpResponse("Potatoes are good!")

def hotdog(request):
    return HttpResponse("Welcome to my hotdog shack! Please select one of the following dogs: 1) Regular 2) Mexican Style 3) Veggie")

def choice(request, menu_id):
    if menu_id == 1:
        option = "Regular"
        price = "$1.50"
    elif menu_id == 2:
        option = "Mexican Style"
        price = "$1.50"
    elif menu_id == 3:
        option = "Veggie"
        price = "$3.50"
    return HttpResponse("You have selected a {0} dog! The total will be {1}".format(option, price))

def hello(request):
    return render(request, 'list/index.html')

def home(request):
    return render(request, 'list/homepage.html')

def contactus(request):
    return render(request, 'list/contactus.html')

def services(request):
    first = "Franco"
    last = "Sanchez"
    top_three = ["Pokemon", "God of War", "League of Legends"]
    context = {'first_name':first, 'last_name':last, 'top_three_games':top_three} #We need to store the variables we want to pass into a dictionary, it's the only way DTL can render it
    return render(request, 'list/services.html', context)

def child(request):
    return render(request, 'list/child.html')