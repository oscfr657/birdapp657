# Generated by Django 2.2 on 2020-05-07 23:30

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('birdapp657', '0054_auto_20200429_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='FontFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('font_family', models.CharField(max_length=50)),
                ('font_format', models.CharField(max_length=50)),
                ('brand', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_fonts', to='birdapp657.BrandingSettings')),
                ('src_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]