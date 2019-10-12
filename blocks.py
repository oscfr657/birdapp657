# -*- coding: utf-8 -*-

from django.utils.html import format_html

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtailmedia.blocks import AbstractMediaChooserBlock


class BirdCodeBlock(blocks.StructBlock):  # TODO: Rename to CodeBirdBlock ?

    code = blocks.TextBlock(required=True)

    class Meta:
        label = 'Code'
        icon = 'code'
        template = 'blocks/code.html'


class RacerBirdBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        required=False,
        features=[
            'h2', 'h3', 'h4', 'h5',
            'bold', 'italic',
            'link', 'document-link',
            'ol', 'ul'])
    image = ImageChooserBlock(required=False)
    right = blocks.BooleanBlock(
        required=False,
        help_text='Image to the right else left')
    bg_color = blocks.CharBlock(
        default='#fff',
        label='Background color')
    text_color = blocks.CharBlock(
        default='#000',
        label='Text color')

    class Meta:
        label = 'Racer'
        icon = 'image'
        template = 'blocks/racer.html'


class HTMLBirdBlock(blocks.StructBlock):

    html = blocks.RawHTMLBlock()

    class Meta:
        label = 'HTML'
        icon = 'code'
        template = 'blocks/html_bird_block.html'


class MediaFileBirdBlock(AbstractMediaChooserBlock):
    # TODO: Implement muted autoplay loop controls ?
    #muted = blocks.BooleanBlock(default=True, help_text='Muted')
    #autoplay = blocks.BooleanBlock(default=False, help_text='Autoplay')
    #loop = blocks.BooleanBlock(default=False, help_text='Loop')
    #controls = blocks.BooleanBlock(default=True, help_text='Controls')

    class Meta:
        label = 'MediaFile'
        icon = 'media'
        template = 'blocks/media_file_bird_block.html'


class FeedBirdBlock(blocks.StructBlock):
    children = blocks.ChoiceBlock(choices=[
            ('c', 'Children'),
            ('d', 'Descendants'),
        ],
        icon='arrow-down',
        required=True)
    
    parent_page = blocks.PageChooserBlock(label='parent page')

    def get_context(self, value):
        context = super(FeedBirdBlock, self).get_context(value)
        if value['children'] == 'c':
            context['feed_posts'] = value[
                'parent_page'].get_children().live().public().not_in_menu().order_by(
                    '-go_live_at')
        elif value['children'] == 'd':
            context['feed_posts'] = value[
                'parent_page'].get_descendants().live().public().not_in_menu().order_by(
                    '-go_live_at')
            print(context)
        return context
    
    class Meta:
        label = 'FeedBlock'
        icon = 'grip'
        template = 'blocks/feed_bird_block.html'