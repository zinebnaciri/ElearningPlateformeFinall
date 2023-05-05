# Generated by Django 4.2.1 on 2023-05-05 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Session",
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
                ("session", models.CharField(max_length=200, unique=True)),
                (
                    "is_current_session",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                ("next_session_begins", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Semester",
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
                    "semester",
                    models.CharField(
                        blank=True,
                        choices=[("First", "First"), ("Second", "Second")],
                        max_length=10,
                    ),
                ),
                (
                    "is_current_semester",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                ("next_semester_begins", models.DateField(blank=True, null=True)),
                (
                    "session",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.session",
                    ),
                ),
            ],
        ),
    ]