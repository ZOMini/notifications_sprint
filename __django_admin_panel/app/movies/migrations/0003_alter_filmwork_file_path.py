# Generated by Django 4.1.2 on 2022-10-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_filmwork_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='file_path',
            field=models.TextField(blank=True, null=True, verbose_name='file_path'),
        ),
    ]