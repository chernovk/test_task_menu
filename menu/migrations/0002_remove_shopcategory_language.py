# Generated by Django 3.1.5 on 2021-01-18 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcategory',
            name='language',
        ),
    ]
