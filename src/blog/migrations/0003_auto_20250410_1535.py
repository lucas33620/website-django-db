# Generated by Django 3.1.7 on 2025-04-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
