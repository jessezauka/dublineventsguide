# Generated by Django 3.0.7 on 2020-07-27 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200727_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='original',
            name='model',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
    ]