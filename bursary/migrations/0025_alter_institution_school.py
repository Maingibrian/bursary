# Generated by Django 4.2.7 on 2023-11-12 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0024_alter_institution_cheque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='school',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bursary.user'),
        ),
    ]
