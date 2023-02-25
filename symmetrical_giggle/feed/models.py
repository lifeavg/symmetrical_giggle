from django.db import models

# Create your models here.


class Post(models.Model):
    header = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=150, unique=True)
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(verbose_name="date published")
    # author
