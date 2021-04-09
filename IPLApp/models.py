from django.db import models

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=15)
    points = models.CharField(max_length=3)
