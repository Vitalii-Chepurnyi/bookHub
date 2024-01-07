from django.shortcuts import render
from django.views import generic
from .models import Listing

# Create your views here.

class MarketList(generic.ListView):
    model = Listing