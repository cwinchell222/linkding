# Generated by Django 5.0.3 on 2024-04-06 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0030_userprofile_bookmarks_per_page"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userprofile",
            old_name="bookmarks_per_page",
            new_name="bookmark_per_page",
        ),
    ]
