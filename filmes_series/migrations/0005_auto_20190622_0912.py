# Generated by Django 2.2.2 on 2019-06-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes_series', '0004_auto_20190622_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]
