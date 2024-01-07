from django.shortcuts import render
from django.views import generic
from .models import Listing

# Create your views here.

class MarketList(generic.ListView):
    queryset = Listing.objects.filter(status=1)
    template_name = "listing_list.html"