# Generated by Django 2.2.9 on 2019-12-25 19:39

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0039_auto_20191218_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='solobirdpage',
            name='header',
            field=wagtail.core.fields.StreamField([('header', wagtail.core.blocks.StructBlock([('muted', wagtail.core.blocks.BooleanBlock(default=True, help_text='Muted', required=False)), ('autoplay', wagtail.core.blocks.BooleanBlock(default=False, help_text='Autoplay', required=False)), ('loop', wagtail.core.blocks.BooleanBlock(default=False, help_text='Loop', required=False)), ('controls', wagtail.core.blocks.BooleanBlock(default=True, help_text='Controls', required=False)), ('block_media', wagtailmedia.blocks.AbstractMediaChooserBlock(null=True, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(null=True, required=False)), ('title', wagtail.core.blocks.CharBlock(null=True, required=False)), ('sub_title', wagtail.core.blocks.CharBlock(null=True, required=False)), ('font_color', wagtail.core.blocks.CharBlock(null=True, required=False))], null=True, required=False))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solobirdpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'superscript', 'subscript', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'blockquote', 'embed', 'image'], null=True, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(null=True, required=False)), ('media', wagtail.core.blocks.StructBlock([('block_width', wagtail.core.blocks.CharBlock(help_text='Block width class', required=False)), ('muted', wagtail.core.blocks.BooleanBlock(default=True, help_text='Muted', required=False)), ('autoplay', wagtail.core.blocks.BooleanBlock(default=False, help_text='Autoplay', required=False)), ('loop', wagtail.core.blocks.BooleanBlock(default=False, help_text='Loop', required=False)), ('controls', wagtail.core.blocks.BooleanBlock(default=True, help_text='Controls', required=False)), ('block_media', wagtailmedia.blocks.AbstractMediaChooserBlock())], null=True, required=False)), ('code', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.TextBlock(required=True))], null=True, required=False)), ('racer', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'link', 'document-link', 'ol', 'ul'], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('right', wagtail.core.blocks.BooleanBlock(help_text='Image to the right else left', required=False)), ('bg_color', wagtail.core.blocks.CharBlock(default='#fff', label='Background color')), ('text_color', wagtail.core.blocks.CharBlock(default='#000', label='Text color'))], null=True, required=False)), ('html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock())], null=True, required=False)), ('feed', wagtail.core.blocks.StructBlock([('block_width', wagtail.core.blocks.CharBlock(help_text='Block width class', required=False)), ('children', wagtail.core.blocks.ChoiceBlock(choices=[('c', 'Children'), ('d', 'Descendants')], icon='arrow-down')), ('parent_page', wagtail.core.blocks.PageChooserBlock(label='parent page')), ('show_title', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('show_intro', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('show_content', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('show_meta', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('show_author', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('show_date', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('number', wagtail.core.blocks.IntegerBlock(required=False))], required=False)), ('page_grid', wagtail.core.blocks.StructBlock([('block_width', wagtail.core.blocks.CharBlock(help_text='Block width class', required=False)), ('children', wagtail.core.blocks.ChoiceBlock(choices=[('c', 'Children'), ('d', 'Descendants')], icon='arrow-down')), ('parent_page', wagtail.core.blocks.PageChooserBlock(label='parent page')), ('show_title', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('show_intro', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('show_content', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('show_meta', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('show_author', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('show_date', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('number', wagtail.core.blocks.IntegerBlock(required=False))], required=False))], blank=True, null=True),
        ),
    ]