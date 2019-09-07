# Generated by Django 2.2.1 on 2019-09-05 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0014_auto_20190903_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionbirdpage',
            name='show_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collectionbirdpage',
            name='show_breadcrumbs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collectionbirdpage',
            name='show_coverImage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='formbirdpage',
            name='show_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='formbirdpage',
            name='show_breadcrumbs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='formbirdpage',
            name='show_coverImage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='htmlbirdpage',
            name='show_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='htmlbirdpage',
            name='show_breadcrumbs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='htmlbirdpage',
            name='show_coverImage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solobirdpage',
            name='show_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solobirdpage',
            name='show_breadcrumbs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solobirdpage',
            name='show_coverImage',
            field=models.BooleanField(default=False),
        ),
    ]