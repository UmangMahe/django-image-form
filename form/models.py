from django.db import models

# Create your models here.

class Form(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media')
