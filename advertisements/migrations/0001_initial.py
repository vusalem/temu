# Generated by Django 5.0.6 on 2024-05-26 06:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Advertisement",
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
                ("title", models.CharField(max_length=32)),
                ("price", models.FloatField()),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(null=True)),
                ("city", models.CharField(max_length=16, null=True)),
            ],
        ),
    ]
