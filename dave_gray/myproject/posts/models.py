from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Post Model explanation here
    """
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self) -> str:
        return self.title
    

