# Generated by Django 4.2.2 on 2023-06-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_ativo_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ativo',
            name='active',
        ),
        migrations.AddField(
            model_name='monitoramento',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
