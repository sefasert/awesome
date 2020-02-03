# Generated by Django 3.0.2 on 2020-02-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20200203_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('D', 'DRAMA'), ('R', 'ROMANCE'), ('C', 'COMEDY'), ('A', 'ACTION')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('TR', 'TOP RATED'), ('MW', 'MOST WATCHED'), ('RA', 'RECENTLY ADDED')], max_length=20),
        ),
        migrations.AlterField(
            model_name='movielink',
            name='type',
            field=models.CharField(choices=[('W', 'WATCH LINK'), ('D', 'DOWNLOAD LINK')], max_length=20),
        ),
    ]
