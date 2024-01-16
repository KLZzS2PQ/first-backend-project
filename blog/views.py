from django.shortcuts import render
from .models import Post


def posts_list(request):
    return render(request, 'blog/posts_list.html', {
        'posts': Post.objects.all()
    })

