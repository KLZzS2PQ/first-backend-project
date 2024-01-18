from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse


def posts_list(request):
    return render(request, 'blog/posts_list.html', {
        'posts': Post.objects.all()
    })

# Страницу rename_post на которой будет 
# форма для изменения имени поста.
def post_like(request):
    if request.method == 'POST':
        post = Post.objects.get(id=request.POST['id'])  
        post.likes += 1
        post.save()
    return redirect('posts_list')
    