from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
