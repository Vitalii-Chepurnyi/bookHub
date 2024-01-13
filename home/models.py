from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Listing(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="market_post"
    )
    description = models.TextField(max_length=1000, unique=False)
    stall_price = models.CharField(max_length=6, unique=False)
    market_date = models.DateField(null=False, blank=True)
    market_time = models.TimeField(null=False, blank=True)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comments(models.Model):
    post = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

class Reservation(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    goods_products = models.BooleanField(default=False)
    foods_products = models.BooleanField(default=False)
    time = models.TimeField(null=False, blank=False)
    email = models.EmailField()
    message = models.TextField()
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation request from {self.name} | {self.surname} arrival: {self.time}"

    