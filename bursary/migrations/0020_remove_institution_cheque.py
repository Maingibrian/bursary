# Generated by Django 4.2.7 on 2023-11-12 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0019_remove_institution_cheque_institution_cheque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='Cheque',
        ),
    ]