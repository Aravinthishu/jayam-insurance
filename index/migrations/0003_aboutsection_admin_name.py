# Generated by Django 5.1.5 on 2025-01-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_aboutsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsection',
            name='admin_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
