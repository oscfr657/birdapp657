# Generated by Django 2.2.7 on 2019-11-24 15:06

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0035_auto_20191124_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandingsettings',
            name='footer',
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
                                'strikethrough',
                                'ol',
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
                        'html',
                        wagtail.core.blocks.StructBlock(
                            [('html', wagtail.core.blocks.RawHTMLBlock())],
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
