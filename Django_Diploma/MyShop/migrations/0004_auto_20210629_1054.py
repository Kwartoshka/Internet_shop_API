# Generated by Django 3.2.4 on 2021-06-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyShop', '0003_auto_20210629_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='updating_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='updating_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='updating_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='updating_date',
            field=models.DateField(),
        ),
    ]
