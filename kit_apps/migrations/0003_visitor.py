# Generated by Django 4.2.5 on 2024-04-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kit_apps", "0002_rename_get_sugetion_studentsuggestion"),
    ]

    operations = [
        migrations.CreateModel(
            name="Visitor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField(default=0)),
            ],
        ),
    ]