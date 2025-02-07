# Generated by Django 5.1.5 on 2025-01-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_insurancesection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('testimonial', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonial/')),
            ],
        ),
    ]
