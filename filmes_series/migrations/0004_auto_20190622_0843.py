# Generated by Django 2.2.2 on 2019-06-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes_series', '0003_auto_20190622_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='cover',
            field=models.FileField(blank=True),
        ),
    ]
