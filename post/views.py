from django.shortcuts import render
from . models import Post


def index(request):
    posts = Post.objects.all().filter(publish=True)

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)


