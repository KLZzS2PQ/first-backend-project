from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    embed_code = models.CharField(max_length=100)

