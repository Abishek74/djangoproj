# Generated by Django 4.2.5 on 2023-09-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0002_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='pno',
            field=models.CharField(max_length=10),
        ),
    ]