# Generated by Django 5.1.5 on 2025-01-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_aboutsection_admin_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='insurance/')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='insurance/')),
                ('icon2', models.ImageField(blank=True, null=True, upload_to='insurance/')),
            ],
        ),
    ]
