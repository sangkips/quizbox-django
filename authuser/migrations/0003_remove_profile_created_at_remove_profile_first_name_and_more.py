# Generated by Django 4.1.4 on 2023-02-02 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authuser", "0002_alter_profile_display_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
    ]