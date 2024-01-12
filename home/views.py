from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Listing, Comments


# Create your views here.

class MarketList(generic.ListView):
    queryset = Listing.objects.filter(status=1)
    template_name = "home/index.html"
    paginate_by = 3

def listing_detail(request, slug):
    queryset = Listing.objects.filter(status=1)
    listing = get_object_or_404(queryset, slug=slug)
    comments = listing.comments.all().order_by("-created_on")
    comment_count = listing.comments.filter(approved=True).count()

    return render(
        request,
        "home/listing_detail.html",
        {"listing": listing,
         "comments": comments,
         "comment_count": comment_count,},
    )