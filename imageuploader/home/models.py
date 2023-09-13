from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length = 50)
    about = models.TextField()
    photo = models.ImageField(upload_to='images')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
