# Generated by Django 4.1.2 on 2022-10-26 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("noteapp", "0005_alter_note_user_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="note", old_name="category", new_name="kategory",
        ),
    ]
