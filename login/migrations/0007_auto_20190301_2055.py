# Generated by Django 2.1.7 on 2019-03-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20190301_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermanage',
            name='c_time',
            field=models.DateField(verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='ordermanage',
            name='e_time',
            field=models.DateField(verbose_name='完成日期'),
        ),
    ]