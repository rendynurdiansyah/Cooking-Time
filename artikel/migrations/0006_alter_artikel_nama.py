# Generated by Django 4.1.1 on 2022-12-20 23:58

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0005_alter_resep_porsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='nama',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]