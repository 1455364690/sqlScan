from django.db import models

# Create your models here.


class user(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    create_time = models.CharField(max_length=100)
    modify_time = models.CharField(max_length=100)
    user_state = models.IntegerField()
    user_role = models.IntegerField()


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
    mistake_detail = models.CharField(max_length=255)
    find_time = models.CharField(max_length=100)
    method = models.CharField(max_length=255)
    extends = models.CharField(max_length=255)


class confidence_rule(models.Model):
    id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    attribute_name = models.CharField(max_length=255)
    rule_a = models.CharField(max_length=255)
    rule_b = models.CharField(max_length=255)
    confidence = models.FloatField()
