from django.db import models

# Create your models here.


class user(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    create_time = models.CharField(max_length=100)
    modify_time = models.CharField(max_length=100)


class task(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    file_name = models.CharField(max_length=255)
    create_time = models.CharField(max_length=100)
    state = models.IntegerField()


class mistake(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    mistake_type = models.CharField(max_length=100)
    mistake_grade = models.CharField(max_length=100)
    find_time = models.CharField(max_length=100)
    method = models.CharField(max_length=255)
