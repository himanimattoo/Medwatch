# Generated by Django 4.2.10 on 2024-03-31 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0002_remove_report_file_reportfile"),
    ]

    operations = [
        migrations.DeleteModel(name="ReportFile",),
    ]
