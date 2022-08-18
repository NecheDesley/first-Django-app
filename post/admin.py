from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'date')
    list_editable = ['publish']



admin.site.register(Post, PostAdmin)
