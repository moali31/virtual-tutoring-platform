# Generated by Django 3.1 on 2020-08-27 12:38

from django.db import migrations, models
import virtual_tutoring.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200827_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', storage=virtual_tutoring.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]
