# Generated by Django 2.1.7 on 2019-03-01 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_ordermanage_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.AddField(
            model_name='user',
            name='statu',
            field=models.CharField(choices=[('ban', '禁用'), ('activation', '激活')], default='禁用', max_length=32),
        ),
    ]
