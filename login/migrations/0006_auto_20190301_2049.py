# Generated by Django 2.1.7 on 2019-03-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20190301_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermanage',
            name='e_time',
            field=models.DateTimeField(null=True, verbose_name='完成日期'),
        ),
    ]
