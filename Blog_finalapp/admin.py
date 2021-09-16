from django.contrib import admin
from .models import Blog_post, log


class Post_admin(admin.ModelAdmin):
    list_display = ('Title', 'slug', 'img', 'content', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['Title', 'content']
    prepopulated_fields = {'slug': ('Title',)}


admin.site.register(Blog_post, Post_admin)
admin.site.register(log)
# Register your models here.
