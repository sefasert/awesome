# Generated by Django 3.0.2 on 2020-02-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='view_count',
            new_name='views_count',
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('C', 'COMEDY'), ('A', 'ACTION'), ('R', 'ROMANCE'), ('D', 'DRAMA')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('GR', 'GERMAN'), ('EN', 'ENGLISH')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('RA', 'RECENTLY ADDED'), ('TR', 'TOP RATED'), ('MW', 'MOST WATCHED')], max_length=20),
        ),
    ]
