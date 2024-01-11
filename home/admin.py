from django.contrib import admin
from .models import Listing, Comments
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Listing)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

# Register your models here.
admin.site.register(Comments)
