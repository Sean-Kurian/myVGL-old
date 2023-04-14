# Generated by Django 4.1.4 on 2023-04-14 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "catalog",
            "0007_developer_publisher_user_rename_comment_comment_text_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Thumbnail",
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
                ("image", models.ImageField(upload_to="thumbnails")),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="thumbnails",
                        to="catalog.game",
                    ),
                ),
            ],
        ),
    ]
