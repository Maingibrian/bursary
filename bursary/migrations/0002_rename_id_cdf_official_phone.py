# Generated by Django 4.2.7 on 2023-11-10 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cdf_official',
            old_name='ID',
            new_name='phone',
        ),
    ]
