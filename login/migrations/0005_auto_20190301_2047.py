# Generated by Django 2.1.7 on 2019-03-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20190301_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermanage',
            name='c_time',
            field=models.DateTimeField(verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='ordermanage',
            name='e_time',
            field=models.DateTimeField(blank=True, verbose_name='完成日期'),
        ),
    ]