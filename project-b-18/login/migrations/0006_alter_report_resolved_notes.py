# Generated by Django 4.2.10 on 2024-04-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0005_remove_report_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="resolved_notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
