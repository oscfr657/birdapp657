# Generated by Django 2.2.1 on 2019-08-29 21:43

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('birdapp657', '0010_auto_20190824_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempRawBirdPage',
            fields=[
                (
                    'page_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='wagtailcore.Page',
                    ),
                ),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('intro', wagtail.fields.RichTextField(blank=True, null=True)),
                ('html', models.TextField(blank=True, null=True)),
                (
                    'coverImage',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='+',
                        to='wagtailimages.Image',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
