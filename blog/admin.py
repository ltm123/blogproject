from django.contrib import admin
from .models import Category, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
