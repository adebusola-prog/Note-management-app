# Generated by Django 4.1.2 on 2022-10-25 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("noteapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="note", options={"ordering": ["-is_pin", "-created_time"]},
        ),
    ]