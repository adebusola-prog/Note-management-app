# Generated by Django 4.1.2 on 2022-10-27 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("noteapp", "0015_alter_note_kategory_alter_note_pdf"),
    ]

    operations = [
        migrations.RenameField(
            model_name="note", old_name="kategory", new_name="category",
        ),
    ]
