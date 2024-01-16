from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/post/images")
    title = models.CharField(max_length=30)
    rating = models.FloatField()
    likes = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
 

