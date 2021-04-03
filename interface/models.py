from django.db import models
import os

class Book(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField()
    photo = models.ImageField()
    qr = models.ImageField(upload_to='qrcodes')




