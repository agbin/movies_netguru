# Generated by Django 2.2.1 on 2019-05-23 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190523_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Awards',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='BoxOffice',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='DVD',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Language',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Metascore',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Plot',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Poster',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Production',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Ratings',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Response',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Website',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Writer',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbID',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbRating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbVotes',
        ),
    ]
