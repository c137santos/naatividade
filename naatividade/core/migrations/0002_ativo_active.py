# Generated by Django 4.2.2 on 2023-06-12 00:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ativo",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]
