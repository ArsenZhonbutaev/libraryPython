# Generated by Django 3.1.3 on 2021-01-25 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='subtitle',
        ),
    ]
