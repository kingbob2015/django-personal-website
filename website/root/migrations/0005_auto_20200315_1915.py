# Generated by Django 3.0.1 on 2020-03-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0004_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.IntegerField(choices=[(1, 'Personal'), (2, 'Professional')]),
        ),
    ]
