# Generated by Django 3.2.6 on 2021-11-14 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='_type',
            new_name='movietype',
        ),
    ]