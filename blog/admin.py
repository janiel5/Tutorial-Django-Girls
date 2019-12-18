from django.contrib import admin
from .models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_date', 'published_date']

admin.site.register(Post, PostAdmin)
