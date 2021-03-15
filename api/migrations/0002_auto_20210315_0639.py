# Generated by Django 3.1.7 on 2021-03-15 05:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='participants',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=10),
        ),
    ]
