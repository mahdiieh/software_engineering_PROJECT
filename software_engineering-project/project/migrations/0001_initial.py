# Generated by Django 3.2.6 on 2021-11-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('director', models.TextField(blank=True, null=True)),
                ('cast', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('rating', models.CharField(max_length=15)),
            ],
        ),
    ]