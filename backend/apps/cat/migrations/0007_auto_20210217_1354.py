# Generated by Django 3.1.6 on 2021-02-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0006_cat_last_time_petted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='last_time_petted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Letztes Mal gestreichelt'),
        ),
    ]