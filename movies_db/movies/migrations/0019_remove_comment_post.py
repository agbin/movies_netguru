# Generated by Django 2.2.1 on 2019-05-24 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_auto_20190524_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]