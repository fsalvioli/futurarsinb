# Generated by Django 4.2.4 on 2024-10-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0020_remove_nosotros_contenido_remove_nosotros_mision_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="NosotrosQueBuscamos",
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
                ("titulo", models.CharField(max_length=200)),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="nosotros/"),
                ),
                ("video", models.URLField(blank=True, null=True)),
                ("publicado", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Que Buscamos",
                "verbose_name_plural": "Que Buscamos Nosotras",
            },
        ),
    ]
