# Generated by Django 2.2 on 2020-03-28 20:26

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0048_auto_20200318_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formbirdpage',
            name='header',
            field=wagtail.fields.StreamField(
                [
                    (
                        'header',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class',
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    'muted',
                                    wagtail.blocks.BooleanBlock(
                                        default=True, help_text='Muted', required=False
                                    ),
                                ),
                                (
                                    'autoplay',
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Autoplay',
                                        required=False,
                                    ),
                                ),
                                (
                                    'loop',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, help_text='Loop', required=False
                                    ),
                                ),
                                (
                                    'controls',
                                    wagtail.blocks.BooleanBlock(
                                        default=True,
                                        help_text='Controls',
                                        required=False,
                                    ),
                                ),
                                (
                                    'block_media',
                                    wagtailmedia.blocks.AbstractMediaChooserBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'image',
                                    wagtail.images.blocks.ImageChooserBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'font_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'text_align',
                                    wagtail.blocks.CharBlock(
                                        default='left', required=False
                                    ),
                                ),
                                (
                                    'text',
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            'h2',
                                            'h3',
                                            'h4',
                                            'h5',
                                            'bold',
                                            'italic',
                                            'link',
                                            'document-link',
                                            'ol',
                                            'ul',
                                        ],
                                        required=False,
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='searchbirdpage',
            name='header',
            field=wagtail.fields.StreamField(
                [
                    (
                        'header',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class',
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    'muted',
                                    wagtail.blocks.BooleanBlock(
                                        default=True, help_text='Muted', required=False
                                    ),
                                ),
                                (
                                    'autoplay',
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Autoplay',
                                        required=False,
                                    ),
                                ),
                                (
                                    'loop',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, help_text='Loop', required=False
                                    ),
                                ),
                                (
                                    'controls',
                                    wagtail.blocks.BooleanBlock(
                                        default=True,
                                        help_text='Controls',
                                        required=False,
                                    ),
                                ),
                                (
                                    'block_media',
                                    wagtailmedia.blocks.AbstractMediaChooserBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'image',
                                    wagtail.images.blocks.ImageChooserBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'font_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'text_align',
                                    wagtail.blocks.CharBlock(
                                        default='left', required=False
                                    ),
                                ),
                                (
                                    'text',
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            'h2',
                                            'h3',
                                            'h4',
                                            'h5',
                                            'bold',
                                            'italic',
                                            'link',
                                            'document-link',
                                            'ol',
                                            'ul',
                                        ],
                                        required=False,
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='solobirdpage',
            name='header',
            field=wagtail.fields.StreamField(
                [
                    (
                        'header',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class',
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    'muted',
                                    wagtail.blocks.BooleanBlock(
                                        default=True, help_text='Muted', required=False
                                    ),
                                ),
                                (
                                    'autoplay',
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Autoplay',
                                        required=False,
                                    ),
                                ),
                                (
                                    'loop',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, help_text='Loop', required=False
                                    ),
                                ),
                                (
                                    'controls',
                                    wagtail.blocks.BooleanBlock(
                                        default=True,
                                        help_text='Controls',
                                        required=False,
                                    ),
                                ),
                                (
                                    'block_media',
                                    wagtailmedia.blocks.AbstractMediaChooserBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'image',
                                    wagtail.images.blocks.ImageChooserBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'font_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'text_align',
                                    wagtail.blocks.CharBlock(
                                        default='left', required=False
                                    ),
                                ),
                                (
                                    'text',
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            'h2',
                                            'h3',
                                            'h4',
                                            'h5',
                                            'bold',
                                            'italic',
                                            'link',
                                            'document-link',
                                            'ol',
                                            'ul',
                                        ],
                                        required=False,
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
