# Generated by Django 2.2.1 on 2019-05-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('Year', models.TextField()),
                ('Rated', models.TextField()),
                ('Released', models.TextField()),
                ('Runtime', models.TextField()),
                ('Genre', models.TextField()),
                ('Director', models.TextField()),
                ('Writer', models.TextField()),
                ('Actors', models.TextField()),
                ('Plot', models.TextField()),
                ('Language', models.TextField()),
                ('Country', models.TextField()),
                ('Awards', models.TextField()),
            ],
        ),
    ]
