# Generated by Django 4.1.8 on 2023-04-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("birdapp657", "0077_remove_birdappsettings_mobile_menu_page_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="formbirdpage",
            name="reCaptcha_key",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="formbirdpage",
            name="reCaptcha_secret",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]