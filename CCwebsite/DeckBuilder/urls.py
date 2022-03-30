from django.urls import path
from . import views

urlpatterns = [
    # Main page
    path('', views.index),
    # Deck build page
    path('deckbuild/', views.deck_builder)
]
