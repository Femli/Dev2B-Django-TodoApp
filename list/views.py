from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

## The functions below will provide specific view to our application
def index(request):
    return HttpResponse("Hello there, thank you for choosing NEST Bagels. We have the following options: 1) White 2) Weat 3)Lamborghini (Our secret recipe!). Please let us know what you would like")

def bagels(request, bagel_id):
    choice = bagel_id
    if bagel_id == 1:
        option = "White"
    elif bagel_id == 2:
        option = "Wheat"
    elif bagel_id == 3:
        option = "Lamborghini"
    return HttpResponse("You have selected %s!" % option)

def lore(request, name):
    return HttpResponse("Five hundred years ago, {0} was born, in the high peak of Mt. Rushmore. {0} was a single child, raised by a single parent, in the vast lands of Midgard. Prophesy foretold that one day, {0} would rise and lead the world to peace. But it could it only be done, once the evil overlord of Musohelheim was slain. {0} would grow up to be one of the strongest warriors of his generation! It is yet to be seen, how the rest of the story unfolds...".format(name))
