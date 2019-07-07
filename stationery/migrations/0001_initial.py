# Generated by Django 2.0.2 on 2019-07-03 06:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deviceman', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='order_record_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('order_status', models.CharField(max_length=40)),
                ('user_list', models.ForeignKey(on_delete=False, to='deviceman.user_list')),
            ],
        ),
        migrations.CreateModel(
            name='order_record_slave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField()),
                ('order_record_master', models.ForeignKey(on_delete=False, to='stationery.order_record_master')),
            ],
        ),
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=40)),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='purchase_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('entryid', models.CharField(max_length=40, unique=True)),
                ('pur_status', models.CharField(default='entering', max_length=40)),
                ('provider', models.ForeignKey(on_delete=False, to='stationery.provider')),
                ('user', models.ForeignKey(default='liuhh', on_delete=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='purchase_slave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('entryid', models.ForeignKey(on_delete=False, to='stationery.purchase_master')),
            ],
        ),
        migrations.CreateModel(
            name='stat_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='stationery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('spec', models.CharField(default='--', max_length=40)),
                ('stock_num', models.IntegerField()),
                ('units', models.CharField(default='个', max_length=6)),
                ('alert_num', models.IntegerField(default=100)),
                ('stat_img', models.ImageField(default='1.jpg', upload_to='image')),
                ('stat_type', models.ForeignKey(on_delete=False, related_name='stat_type_name', to='stationery.stat_type')),
            ],
        ),
        migrations.AddField(
            model_name='purchase_slave',
            name='stationery',
            field=models.ForeignKey(on_delete=False, to='stationery.stationery'),
        ),
        migrations.AddField(
            model_name='order_record_slave',
            name='stationery',
            field=models.ForeignKey(on_delete=False, to='stationery.stationery'),
        ),
        migrations.AddField(
            model_name='cart',
            name='stationery',
            field=models.ForeignKey(on_delete=False, to='stationery.stationery'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_list',
            field=models.ForeignKey(on_delete=False, to='deviceman.user_list'),
        ),
    ]
