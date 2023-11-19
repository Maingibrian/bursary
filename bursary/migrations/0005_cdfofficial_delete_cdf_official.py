# Generated by Django 4.2.7 on 2023-11-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0004_rename_id_cdf_official_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='cdfofficial',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('phone', models.IntegerField(max_length=255, null=True)),
                ('Name', models.CharField(max_length=255, null=True)),
                ('designation', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='cdf_official',
        ),
    ]