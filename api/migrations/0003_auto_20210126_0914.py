# Generated by Django 3.1.5 on 2021-01-26 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210126_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='seniorhigh',
            name='Student_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='seniorhigh',
            name='Teacher',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
