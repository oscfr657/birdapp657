# Generated by Django 2.2.7 on 2019-12-18 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0038_auto_20191215_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='formbirdpage',
            name='transparent_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='searchbirdpage',
            name='transparent_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solobirdpage',
            name='transparent_header',
            field=models.BooleanField(default=False),
        ),
    ]