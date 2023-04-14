# Generated by Django 4.1.4 on 2023-04-14 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0008_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="likes",
            field=models.ManyToManyField(related_name="liked_games", to="catalog.user"),
        ),
        migrations.AddField(
            model_name="game",
            name="ratings",
            field=models.ManyToManyField(
                related_name="rated_games", through="catalog.Rating", to="catalog.user"
            ),
        ),
        migrations.CreateModel(
            name="Like",
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
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="catalog.game"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="catalog.user"
                    ),
                ),
            ],
        ),
    ]
