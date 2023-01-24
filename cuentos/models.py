

from django.db import models
from django.contrib.auth.models import User
from .utils import validate_custom_date_format


class Author(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    date = models.CharField(max_length=10,
                            validators=[validate_custom_date_format])


class Cuento(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.CharField(max_length=10,
                                      validators=[validate_custom_date_format])
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.published_date}) by {self.author}"


class Comentario(models.Model):
    cuento = models.ForeignKey(Cuento, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Favorite(models.Model):
    cuento = models.ForeignKey(Cuento, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)