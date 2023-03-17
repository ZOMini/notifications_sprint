# Generated by Django 4.1.2 on 2022-10-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_filmwork_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(choices=[('movie', 'Movie'), ('tv_show', 'Tv Show')], max_length=32, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.TextField(choices=[('actor', 'Actor'), ('writer', 'Writer'), ('director', 'Director')], null=True, verbose_name='role'),
        ),
    ]