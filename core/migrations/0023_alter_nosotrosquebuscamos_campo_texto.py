# Generated by Django 4.2.4 on 2024-10-01 21:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0022_alter_nosotros_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nosotrosquebuscamos",
            name="campo_texto",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
