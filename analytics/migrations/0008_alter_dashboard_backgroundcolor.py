# Generated by Django 4.0.5 on 2022-08-14 20:33

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_alter_dashboard_backgroundcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='backgroundColor',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]
