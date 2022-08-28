# Generated by Django 4.1 on 2022-08-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "video_id",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Video ID"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "thumbnail",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Thumbnails of different resolutions.",
                        verbose_name="Thumbnail",
                    ),
                ),
                (
                    "published_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Published at"
                    ),
                ),
            ],
            options={
                "verbose_name": "Video",
                "verbose_name_plural": "Videos",
            },
        ),
    ]
