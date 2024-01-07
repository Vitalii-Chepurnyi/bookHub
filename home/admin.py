from django.contrib import admin
from .models import Listing, Comments

# Register your models here.
admin.site.register(Listing)

admin.site.register(Comments)