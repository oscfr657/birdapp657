# Generated by Django 3.1.6 on 2021-05-27 18:21

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0070_auto_20210527_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solobirdpage',
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
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    'block_width',
                                    wagtail.core.blocks.CharBlock(
                                        help_text='Block width class', required=False
                                    ),
                                ),
                                (
                                    'muted',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=True, help_text='Muted', required=False
                                    ),
                                ),
                                (
                                    'autoplay',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Autoplay',
                                        required=False,
                                    ),
                                ),
                                (
                                    'loop',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, help_text='Loop', required=False
                                    ),
                                ),
                                (
                                    'controls',
                                    wagtail.core.blocks.BooleanBlock(
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
                        wagtail.core.blocks.StructBlock(
                            [('code', wagtail.core.blocks.TextBlock(required=True))],
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
                    (
                        'hero',
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.core.blocks.CharBlock(
                                        help_text='Block class',
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    'muted',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=True, help_text='Muted', required=False
                                    ),
                                ),
                                (
                                    'autoplay',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Autoplay',
                                        required=False,
                                    ),
                                ),
                                (
                                    'loop',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, help_text='Loop', required=False
                                    ),
                                ),
                                (
                                    'controls',
                                    wagtail.core.blocks.BooleanBlock(
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
                                    'full_screen',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Full screen',
                                        required=False,
                                    ),
                                ),
                                (
                                    'font_color',
                                    wagtail.core.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.core.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'text_align',
                                    wagtail.core.blocks.CharBlock(
                                        default='left', required=False
                                    ),
                                ),
                                (
                                    'text',
                                    wagtail.core.blocks.RichTextBlock(
                                        features=[
                                            'h1',
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
                                    'button_link',
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                'font_color',
                                                wagtail.core.blocks.CharBlock(
                                                    null=True, required=False
                                                ),
                                            ),
                                            (
                                                'bg_color',
                                                wagtail.core.blocks.CharBlock(
                                                    null=True, required=False
                                                ),
                                            ),
                                            (
                                                'page_link',
                                                wagtail.core.blocks.PageChooserBlock(
                                                    help_text='Link to a page.',
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                'external_link',
                                                wagtail.core.blocks.URLBlock(
                                                    help_text='Link to a URL.',
                                                    label='Link URL',
                                                    max_length=200,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                'text',
                                                wagtail.core.blocks.CharBlock(
                                                    help_text='Link text',
                                                    null=True,
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        null=True,
                                        required=False,
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'hero_bt',
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.core.blocks.CharBlock(
                                        help_text='Block class',
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    'full_screen',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Full screen',
                                        required=False,
                                    ),
                                ),
                                (
                                    'font_color',
                                    wagtail.core.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.core.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'text_align',
                                    wagtail.core.blocks.CharBlock(
                                        default='left', required=False
                                    ),
                                ),
                                (
                                    'text',
                                    wagtail.core.blocks.RichTextBlock(
                                        features=[
                                            'h1',
                                            'h2',
                                            'h3',
                                            'h4',
                                            'bold',
                                            'italic',
                                            'link',
                                            'document-link',
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    'button_link',
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                'font_color',
                                                wagtail.core.blocks.CharBlock(
                                                    null=True, required=False
                                                ),
                                            ),
                                            (
                                                'bg_color',
                                                wagtail.core.blocks.CharBlock(
                                                    null=True, required=False
                                                ),
                                            ),
                                            (
                                                'page_link',
                                                wagtail.core.blocks.PageChooserBlock(
                                                    help_text='Link to a page.',
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                'external_link',
                                                wagtail.core.blocks.URLBlock(
                                                    help_text='Link to a URL.',
                                                    label='Link URL',
                                                    max_length=200,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                'text',
                                                wagtail.core.blocks.CharBlock(
                                                    help_text='Link text',
                                                    null=True,
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        null=True,
                                        required=False,
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'feed',
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.core.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                                (
                                    'children',
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ('c', 'Children'),
                                            ('d', 'Descendants'),
                                        ],
                                        icon='arrow-down',
                                    ),
                                ),
                                (
                                    'parent_page',
                                    wagtail.core.blocks.PageChooserBlock(
                                        label='parent page'
                                    ),
                                ),
                                (
                                    'exclude',
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.PageChooserBlock(
                                            label='Exclude page'
                                        ),
                                        default=[],
                                        required=False,
                                    ),
                                ),
                                (
                                    'tags',
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.CharBlock(label='Tag'),
                                        required=False,
                                    ),
                                ),
                                (
                                    'show_title',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=True, required=False
                                    ),
                                ),
                                (
                                    'show_intro',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_content',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_meta',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_author',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_date',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'use_grid_template',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='white', label='Background color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='black', label='Text color'
                                    ),
                                ),
                                (
                                    'max_number',
                                    wagtail.core.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        'grid',
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.core.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                                (
                                    'children',
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ('c', 'Children'),
                                            ('d', 'Descendants'),
                                        ],
                                        icon='arrow-down',
                                    ),
                                ),
                                (
                                    'parent_page',
                                    wagtail.core.blocks.PageChooserBlock(
                                        label='parent page'
                                    ),
                                ),
                                (
                                    'exclude',
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.PageChooserBlock(
                                            label='Exclude page'
                                        ),
                                        required=False,
                                    ),
                                ),
                                (
                                    'tags',
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.CharBlock(label='Tag'),
                                        required=False,
                                    ),
                                ),
                                (
                                    'show_meta',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=True, required=False
                                    ),
                                ),
                                (
                                    'title_page',
                                    wagtail.core.blocks.PageChooserBlock(
                                        label='Title page', required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='white', label='Background color'
                                    ),
                                ),
                                (
                                    'title_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='black', label='Title color'
                                    ),
                                ),
                                (
                                    'bg_text_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='white', label='Background text color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='black', label='Text color'
                                    ),
                                ),
                                (
                                    'max_number',
                                    wagtail.core.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        'simplegrid',
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.core.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                                (
                                    'children',
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ('c', 'Children'),
                                            ('d', 'Descendants'),
                                        ],
                                        icon='arrow-down',
                                    ),
                                ),
                                (
                                    'parent_page',
                                    wagtail.core.blocks.PageChooserBlock(
                                        label='parent page'
                                    ),
                                ),
                                (
                                    'exclude',
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.PageChooserBlock(
                                            label='Exclude page'
                                        ),
                                        required=False,
                                    ),
                                ),
                                (
                                    'tags',
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.CharBlock(label='Tag'),
                                        required=False,
                                    ),
                                ),
                                (
                                    'show_meta',
                                    wagtail.core.blocks.BooleanBlock(
                                        default=True, required=False
                                    ),
                                ),
                                (
                                    'title_page',
                                    wagtail.core.blocks.PageChooserBlock(
                                        label='Title page', required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='white', label='Background color'
                                    ),
                                ),
                                (
                                    'title_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='black', label='Title color'
                                    ),
                                ),
                                (
                                    'bg_text_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='white', label='Background text color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='black', label='Text color'
                                    ),
                                ),
                                (
                                    'max_number',
                                    wagtail.core.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        'racer',
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    'text',
                                    wagtail.core.blocks.RichTextBlock(
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
                                    wagtail.core.blocks.PageChooserBlock(
                                        help_text='Link image to a page.',
                                        required=False,
                                    ),
                                ),
                                (
                                    'external_image_link',
                                    wagtail.core.blocks.URLBlock(
                                        help_text='Link image to a URL.',
                                        label='Link URL',
                                        max_length=200,
                                        required=False,
                                    ),
                                ),
                                (
                                    'right',
                                    wagtail.core.blocks.BooleanBlock(
                                        help_text='Image to the right else left',
                                        required=False,
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='#fff', label='Background color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='#000', label='Text color'
                                    ),
                                ),
                                (
                                    'block_class',
                                    wagtail.core.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'simpleracer',
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    'text',
                                    wagtail.core.blocks.RichTextBlock(
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
                                    wagtail.core.blocks.PageChooserBlock(
                                        help_text='Link image to a page.',
                                        required=False,
                                    ),
                                ),
                                (
                                    'external_image_link',
                                    wagtail.core.blocks.URLBlock(
                                        help_text='Link image to a URL.',
                                        label='Link URL',
                                        max_length=200,
                                        required=False,
                                    ),
                                ),
                                (
                                    'right',
                                    wagtail.core.blocks.BooleanBlock(
                                        help_text='Image to the right else left',
                                        required=False,
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='#fff', label='Background color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.core.blocks.CharBlock(
                                        default='#000', label='Text color'
                                    ),
                                ),
                                (
                                    'block_class',
                                    wagtail.core.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                            ],
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
