# Generated by Django 2.1.7 on 2019-02-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190228_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermanage',
            name='price',
            field=models.SmallIntegerField(default=0, verbose_name='订单金额'),
        ),
    ]
