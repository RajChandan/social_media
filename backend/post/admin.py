from django.contrib import admin
from .models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["author","content"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post","author","content"]

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)