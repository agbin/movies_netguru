# Generated by Django 2.2.1 on 2019-05-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20190523_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='BoxOffice',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='DVD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='Metascore',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='Poster',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='Production',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='Ratings',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='Response',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='Type',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='Website',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdbID',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdbRating',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdbVotes',
            field=models.TextField(blank=True),
        ),
    ]
