# Generated by Django 4.2.7 on 2023-11-14 12:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bursary', '0026_alter_institution_cheque'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='University',
        ),
    ]
