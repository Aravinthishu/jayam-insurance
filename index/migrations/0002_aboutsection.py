# Generated by Django 5.1.5 on 2025-01-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/')),
                ('admin_image', models.ImageField(blank=True, null=True, upload_to='about/')),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
