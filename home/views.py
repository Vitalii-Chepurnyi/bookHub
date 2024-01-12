from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Listing, Comments
from .forms import CommentForm


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
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = listing
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for your comment!'
            )


    comment_form = CommentForm()

    return render(
        request,
        "home/listing_detail.html",
        {"listing": listing,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,},
    )