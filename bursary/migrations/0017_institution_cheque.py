# Generated by Django 4.2.7 on 2023-11-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0016_user_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='cheque',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
