# Generated by Django 3.0.6 on 2020-05-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200519_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='original',
            name='date',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='original',
            name='price_max',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='original',
            name='price_min',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='original',
            name='votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
