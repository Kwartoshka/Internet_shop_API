# Generated by Django 3.2.4 on 2021-06-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='updating_date',
            field=models.DateField(default=None),
        ),
    ]