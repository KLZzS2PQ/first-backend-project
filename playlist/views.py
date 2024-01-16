from django.shortcuts import render, redirect
from .models import Video


def playlist(request):
    return render(request, "playlist/playlist.html", {
        "videos": Video.objects.all(),
        })


def create_video(request):
    if request.method == 'POST': 
        embed_code = request.POST['embed_code']
        title = request.POST['title']
        Video.objects.create(
            embed_code=embed_code,
            title=title
        )
        return redirect('playlist')
    return render(request, "playlist/create_video.html")
    
