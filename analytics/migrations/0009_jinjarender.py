# Generated by Django 4.1 on 2022-08-23 06:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0008_alter_dashboard_backgroundcolor"),
    ]

    operations = [
        migrations.CreateModel(
            name="JinjaRender",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
    ]
