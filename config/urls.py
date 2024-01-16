from django.contrib import admin
from django.urls import path
from Core.views import example, example2, magic_number
from django.conf import settings
from django.conf.urls.static import static
from blog.views import posts_list
from playlist.views import playlist
from playlist.views import create_video
from pprint import pprint
def sum():
    return 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('examplderhserthwetrjwrtje_1/', example, name='example'),
    path('example2/', example2),
    path('magic_number/', magic_number),
    path('posts_list/', posts_list, name='postlist'),
    path('playlist/', playlist, name='playlist'),
    path('create_video/', create_video),
]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    pprint(urlpatterns)