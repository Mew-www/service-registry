# Generated by Django 3.0.6 on 2020-06-05 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="endpoint_url",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
