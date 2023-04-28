# Generated by Django 2.2 on 2020-03-02 22:22

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0043_auto_20200228_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solobirdpage',
            name='body',
            field=wagtail.fields.StreamField(
                [
                    (
                        'paragraph',
                        wagtail.blocks.RichTextBlock(
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
                        'media',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_width',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block width class', required=False
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
                                    wagtailmedia.blocks.AbstractMediaChooserBlock(),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'code',
                        wagtail.blocks.StructBlock(
                            [('code', wagtail.blocks.TextBlock(required=True))],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'racer',
                        wagtail.blocks.StructBlock(
                            [
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
                                (
                                    'image',
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    'page_image_link',
                                    wagtail.blocks.PageChooserBlock(
                                        help_text='Link image to a page.',
                                        required=False,
                                    ),
                                ),
                                (
                                    'external_image_link',
                                    wagtail.blocks.URLBlock(
                                        help_text='Link image to a URL.',
                                        label='Link URL',
                                        max_length=200,
                                        required=False,
                                    ),
                                ),
                                (
                                    'right',
                                    wagtail.blocks.BooleanBlock(
                                        help_text='Image to the right else left',
                                        required=False,
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        default='#fff', label='Background color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.blocks.CharBlock(
                                        default='#000', label='Text color'
                                    ),
                                ),
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'html',
                        wagtail.blocks.StructBlock(
                            [('html', wagtail.blocks.RawHTMLBlock())],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'feed',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_width',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block width class', required=False
                                    ),
                                ),
                                (
                                    'children',
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ('c', 'Children'),
                                            ('d', 'Descendants'),
                                        ],
                                        icon='arrow-down',
                                    ),
                                ),
                                (
                                    'parent_page',
                                    wagtail.blocks.PageChooserBlock(
                                        label='parent page'
                                    ),
                                ),
                                (
                                    'show_title',
                                    wagtail.blocks.BooleanBlock(
                                        default=True, required=False
                                    ),
                                ),
                                (
                                    'show_intro',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_content',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_meta',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_author',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_date',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'number',
                                    wagtail.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        'page_grid',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_width',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block width class', required=False
                                    ),
                                ),
                                (
                                    'children',
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ('c', 'Children'),
                                            ('d', 'Descendants'),
                                        ],
                                        icon='arrow-down',
                                    ),
                                ),
                                (
                                    'parent_page',
                                    wagtail.blocks.PageChooserBlock(
                                        label='parent page'
                                    ),
                                ),
                                (
                                    'show_title',
                                    wagtail.blocks.BooleanBlock(
                                        default=True, required=False
                                    ),
                                ),
                                (
                                    'show_intro',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_content',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_meta',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_author',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_date',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'number',
                                    wagtail.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
