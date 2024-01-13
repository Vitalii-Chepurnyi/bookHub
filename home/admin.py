from django.contrib import admin
from .models import Listing, Comments, Reservation
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Listing)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

@admin.register(Reservation)
class Reservation(admin.ModelAdmin):

    list_display = ('name', 'message', 'time')


admin.site.register(Comments)
