# Generated by Django 3.0.1 on 2020-03-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0006_auto_20200315_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.IntegerField(choices=[(0, 'Personal'), (1, 'Professional')]),
        ),
    ]
