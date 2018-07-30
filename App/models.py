from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)
    create = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class User(models.Model):
    SEX = (
        ("M","男性"),
        ("F","女性"),
        ("U","女性")
    )
    user_name = models.CharField(max_length=32)
    user_icon = models.ImageField()
    password = models.IntegerField(max_length=128)
    user_sex = models.CharField(max_length=8,choices=SEX)
    user_age = models.CharField(max_length=16)
