# Generated by Django 4.1.7 on 2023-04-23 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_contactus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contactus',
            new_name='Contact',
        ),
    ]