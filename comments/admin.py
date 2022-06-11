from django.contrib import admin

# Register your models here.
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('name', 'email', 'body')