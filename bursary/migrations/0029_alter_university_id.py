# Generated by Django 4.2.7 on 2023-11-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0028_alter_university_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
