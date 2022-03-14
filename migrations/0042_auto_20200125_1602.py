# Generated by Django 2.2.9 on 2020-01-25 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('birdapp657', '0041_brandingsettings_extra_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandingsettings',
            name='extra_css',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtaildocs.Document',
            ),
        ),
        migrations.AddField(
            model_name='brandingsettings',
            name='extra_js',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='wagtaildocs.Document',
            ),
        ),
    ]
