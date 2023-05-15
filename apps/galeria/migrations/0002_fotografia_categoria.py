# Generated by Django 4.1 on 2023-03-31 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("NEBULOSA", "Nebulosa"),
                    ("DIA", "Dia"),
                    ("NOITE", "Noite"),
                    ("PLANETA", "Planeta"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
