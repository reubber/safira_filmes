# Generated by Django 2.2.2 on 2019-06-19 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes_series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='cover',
            field=models.FileField(default='arquivo.png', upload_to='cover_filmes'),
            preserve_default=False,
        ),
    ]
