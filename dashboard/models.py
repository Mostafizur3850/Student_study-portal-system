from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from tables import Description

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"
        
    def __str__(self):
        return self.title
    
    
# create a class for Homework 

class Homework(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    subject = models.CharField(max_length=50)
    tiltle = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    