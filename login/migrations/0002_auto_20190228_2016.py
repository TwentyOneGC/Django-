# Generated by Django 2.1.7 on 2019-02-28 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=128, unique=True, verbose_name='订单号')),
                ('customer_ser', models.CharField(max_length=64, verbose_name='客服')),
                ('author', models.CharField(max_length=64, verbose_name='作者')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('o_detail', models.TextField(verbose_name='订单详情')),
                ('status', models.SmallIntegerField(choices=[(0, '制作'), (1, '测试'), (2, '退单'), (3, '完成')], default=0, verbose_name='订单状态')),
                ('e_time', models.DateTimeField(auto_now=True, verbose_name='完成日期')),
            ],
            options={
                'verbose_name': '订单总表',
                'verbose_name_plural': '订单总表',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': '商铺',
                'verbose_name_plural': '商铺',
            },
        ),
        migrations.AddField(
            model_name='ordermanage',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Store', verbose_name='店铺名称'),
        ),
    ]
