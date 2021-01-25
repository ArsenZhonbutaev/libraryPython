from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    genre = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


