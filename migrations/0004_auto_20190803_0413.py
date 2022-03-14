# Generated by Django 2.2.1 on 2019-08-03 02:13

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0003_auto_20190803_0037'),
    ]

    operations = [
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
