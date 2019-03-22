from django.db import models

# Create your models here.


class test(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
