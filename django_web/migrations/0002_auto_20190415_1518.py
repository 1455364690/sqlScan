# Generated by Django 2.1.7 on 2019-04-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mistake',
            name='mistake_detail',
            field=models.CharField(max_length=2048),
        ),
    ]
