# Generated by Django 4.2.7 on 2023-11-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0023_alter_institution_cheque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='Cheque',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
