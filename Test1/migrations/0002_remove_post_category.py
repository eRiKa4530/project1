# Generated by Django 4.1.6 on 2023-02-02 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
