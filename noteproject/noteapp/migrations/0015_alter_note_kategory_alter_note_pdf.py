# Generated by Django 4.1.2 on 2022-10-27 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("noteapp", "0014_note_pdf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="kategory",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="noteapp.category",
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="pdf",
            field=models.FileField(
                help_text="You can upload your files here", upload_to=""
            ),
        ),
    ]
