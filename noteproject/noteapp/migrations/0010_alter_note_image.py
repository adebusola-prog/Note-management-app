# Generated by Django 4.1.2 on 2022-10-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("noteapp", "0009_alter_note_user_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]