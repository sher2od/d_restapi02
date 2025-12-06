from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser

User =  get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description  = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description  = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name






