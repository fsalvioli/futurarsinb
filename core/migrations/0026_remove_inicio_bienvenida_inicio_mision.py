# Generated by Django 4.2.4 on 2024-10-08 21:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0025_alter_nosotrosquebuscamos_campo_texto"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inicio",
            name="bienvenida",
        ),
        migrations.AddField(
            model_name="inicio",
            name="mision",
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
