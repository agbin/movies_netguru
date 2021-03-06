# Generated by Django 2.2.1 on 2019-05-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_auto_20190523_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='actor_name',
            field=models.TextField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Actors',
            field=models.ManyToManyField(blank=True, to='movies.Actor'),
        ),
    ]
