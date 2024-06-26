from django.db import models
from django.contrib.auth.models import User




class Author(models.Model):
    fullname = models.CharField(max_length=50)
    date_born= models.CharField(max_length=50)
    location_born= models.CharField(max_length=150)
    bio= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='tag of username')
         ]

    def __str__(self):
        return f"{self.name}"


class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote
  