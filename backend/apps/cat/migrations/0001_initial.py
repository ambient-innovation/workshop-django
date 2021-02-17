# Generated by Django 3.1.6 on 2021-02-17 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Hideout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Erstellt am')),
                ('lastmodified_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Zuletzt geändert am')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cat_cat_created', to=settings.AUTH_USER_MODEL, verbose_name='Erstellt von')),
                ('current_hideout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cat.hideout', verbose_name='Aktuelles Versteck')),
                ('favourite_food', models.ManyToManyField(related_name='cats', to='cat.Food', verbose_name='Lieblingsessen')),
                ('lastmodified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cat_cat_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Zuletzt geändert von')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Besitzer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]