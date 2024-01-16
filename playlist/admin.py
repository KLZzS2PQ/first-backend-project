from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'embed_code', 'created_at', ) 
    list_editable = ('embed_code',  )
