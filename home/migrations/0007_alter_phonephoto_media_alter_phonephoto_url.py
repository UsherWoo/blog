# Generated by Django 5.2.1 on 2025-06-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_phonemaker_phonemodel_phone_phonephoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonephoto',
            name='media',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='phonephoto',
            name='url',
            field=models.URLField(default='http://'),
        ),
    ]
