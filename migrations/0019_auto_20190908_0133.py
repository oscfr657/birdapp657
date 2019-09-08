# Generated by Django 2.2.1 on 2019-09-07 23:33

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('birdapp657', '0018_auto_20190908_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchbirdpage',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='searchbirdpage',
            name='coverImage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='searchbirdpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='searchbirdpage',
            name='show_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='searchbirdpage',
            name='show_breadcrumbs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='searchbirdpage',
            name='show_coverImage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='searchbirdpage',
            name='show_date',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='searchbirdpage',
            name='show_meta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='searchbirdpage',
            name='show_title',
            field=models.BooleanField(default=True),
        ),
    ]
