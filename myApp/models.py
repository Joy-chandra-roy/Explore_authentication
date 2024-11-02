from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    dep=models.CharField(max_length=100)
    roll=models.IntegerField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name}"