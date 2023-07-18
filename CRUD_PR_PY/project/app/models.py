from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    author = models.CharField(max_length=255,blank=False,null=False)
    genre = models.CharField(max_length=255,blank=False,null=False)
    age=models.IntegerField()
    publisher = models.CharField(max_length=255,blank=False,null=False)
    
    def __str__(self) :
        return self.name