from django.contrib import admin
from django.urls import path
from Core.views import example, example2, magic_number
from django.conf import settings
from django.conf.urls.static import static
from blog.views import posts_list, post_like 
from playlist.views import playlist
from playlist.views import create_video

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exampld1/', example, name='example'),
    path('example2/', example2),
    path('magic_number/', magic_number),
    path('posts_list/', posts_list, name='posts_list'),
    path('playlist/', playlist, name='playlist'),
    path('create_video/', create_video),
    path('post_like/', post_like, name='post_like')
]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  