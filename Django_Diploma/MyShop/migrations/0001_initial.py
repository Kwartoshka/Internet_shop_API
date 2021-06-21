# Generated by Django 3.2.4 on 2021-06-21 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('updating_date', models.DateField(default=models.DateField(auto_now_add=True))),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('mark', models.IntegerField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('updating_date', models.DateField(default=models.DateField(auto_now_add=True))),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyShop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(choices=[('NEW', 'Новый'), ('IN_PROGRESS', 'В процессе'), ('DONE', 'Выполнен')], default='NEW')),
                ('order_sum', models.IntegerField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('updating_date', models.DateField(default=models.DateField(auto_now_add=True))),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(default='')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('updating_date', models.DateField(default=models.DateField(auto_now_add=True))),
                ('products', models.ManyToManyField(to='MyShop.Product')),
            ],
        ),
    ]
