# Generated by Django 3.1.5 on 2021-01-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='juniorhigh',
            name='Student_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='juniorhigh',
            name='Teacher',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='juniorhigh',
            name='Section',
            field=models.CharField(choices=[('7 Rizal', '7 Rizal'), ('7 Bonifacio', '7 Bonifacio'), ('7 Del Pilar', '7 Del Pilar'), ('8 Nakpil', '8 Nakpil'), ('8 Bernal', '8 Bernal'), ('8 Joaquin', '8 Joaquin'), ('9 Shakespeare', '9 Shakespeare'), ('9 Dickens', '9 Dickens'), ('9 Twain', '9 Twain'), ('10 Einstein', '10 Einstein'), ('10 Franklin', '10 Franklin'), ('10 Newton', '10 Newton')], max_length=100),
        ),
    ]
