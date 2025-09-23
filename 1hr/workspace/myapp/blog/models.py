from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(blanl=True) # default max_length=200, blank=True means its a nullabe column

    def __str__(self):
        return f'{self.title}'

