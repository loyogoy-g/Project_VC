# Generated by Django 3.1.5 on 2021-01-25 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_seniorhigh_shfirstquarter_shsecondquarter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourthquarter',
            name='Grade',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='secondquarter',
            name='Grade',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='shsecondquarter',
            name='Grade',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='thirdquarter',
            name='Grade',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
