from django.shortcuts import render
from django.http import HttpResponse
from httplib2 import Http


# Create your views here.
def index(request):
    return render(request, './base.html')


def deck_builder(request):
    return HttpResponse("This is where you build your decks")