from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from httplib2 import Http
from glob import glob
import json
from DeckBuilder.tools import process_deckbuilder_request

import requests
# Create your views here.
def index(request):
    return HttpResponse("MAinPAGE")


def deck_builder(request):
    context = process_deckbuilder_request(request)
    if request.method == "GET":
        pass
    else:
        return HttpResponse("POSHELWON")
    return render(request, './base.html', context=context)

def request_page(request):
    print("hi")
    return HttpResponse("buttonClick")