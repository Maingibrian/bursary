# Generated by Django 4.2.7 on 2023-11-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0005_cdfofficial_delete_cdf_official'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdfofficial',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]