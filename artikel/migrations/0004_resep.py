# Generated by Django 4.1.1 on 2022-12-20 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0003_alter_artikel_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porsi', models.TextField()),
                ('title', models.CharField(max_length=1000)),
                ('kunci', models.CharField(max_length=100)),
                ('tingkat', models.CharField(max_length=100)),
                ('waktu', models.TextField()),
                ('gambar', models.ImageField(upload_to='')),
            ],
        ),
    ]
