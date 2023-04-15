from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField(max_length=50)
    date = models.DateField()
    author = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
