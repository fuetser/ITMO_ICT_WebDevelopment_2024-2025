# Generated by Django 5.1.2 on 2024-11-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "project_first_app",
            "0002_alter_ownership_end_date_alter_ownership_start_date",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="driverlicense",
            name="issue_date",
            field=models.DateField(auto_now=True),
        ),
    ]
