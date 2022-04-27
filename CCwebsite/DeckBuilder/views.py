from django.shortcuts import render
from django.http import HttpResponse
from DeckBuilder.tools import process_deckbuilder_request


# Create your views here.
def index(request):
    return render(request, './base.html')


def deck_builder(request):
    context = process_deckbuilder_request(request)
    if request.method == "GET":
        pass
    else:
        return HttpResponse("POSHELWON")
    return render(request, './DeckBuilderPage.html', context=context)


def request_page(request):
    print("hi")
    return HttpResponse("buttonClick")
