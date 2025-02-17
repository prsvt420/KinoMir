# Generated by Django 5.1.4 on 2024-12-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
                "db_table": "genres",
                "db_table_comment": "Таблица содержит список жанров",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Person",
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
                ("first_name", models.CharField(max_length=255, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=255, verbose_name="Фамилия")),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="film_participants/",
                        verbose_name="Фото",
                    ),
                ),
            ],
            options={
                "verbose_name": "Человек",
                "verbose_name_plural": "Люди",
                "db_table": "persons",
                "db_table_comment": "Таблица содержит список людей",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
                "db_table": "tags",
                "db_table_comment": "Таблица содержит список тегов",
                "ordering": ("id",),
            },
        ),
    ]
