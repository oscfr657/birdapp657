# Generated by Django 2.2.1 on 2019-08-07 22:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0004_auto_20190803_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawBirdPage',
            fields=[
                (
                    'birdbasepage_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='birdapp657.BirdBasePage',
                    ),
                ),
                ('html', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('birdapp657.birdbasepage',),
        ),
        migrations.AlterField(
            model_name='birdpage',
            name='body',
            field=wagtail.core.fields.StreamField(
                [
                    (
                        'paragraph',
                        wagtail.core.blocks.RichTextBlock(
                            features=[
                                'h2',
                                'h3',
                                'h4',
                                'bold',
                                'italic',
                                'superscript',
                                'subscript',
                                'strikethroughol',
                                'ul',
                                'hr',
                                'link',
                                'document-link',
                                'blockquote',
                                'embed',
                                'image',
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'image',
                        wagtail.images.blocks.ImageChooserBlock(
                            null=True, required=False
                        ),
                    ),
                    (
                        'code',
                        wagtail.core.blocks.StructBlock(
                            [('code', wagtail.core.blocks.TextBlock(required=True))],
                            null=True,
                            required=False,
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
