# Generated by Django 3.1.3 on 2020-11-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dapp',
            name='description',
            field=models.TextField(default='', max_length=20),
        ),
    ]
