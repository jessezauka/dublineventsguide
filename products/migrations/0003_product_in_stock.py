# Generated by Django 3.0.6 on 2020-05-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200515_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
