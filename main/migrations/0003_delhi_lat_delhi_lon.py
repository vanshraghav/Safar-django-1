# Generated by Django 4.1.7 on 2023-04-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_delhi_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='delhi',
            name='lat',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delhi',
            name='lon',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]