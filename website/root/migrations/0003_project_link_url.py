# Generated by Django 3.0.1 on 2020-03-15 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_project_projecttechnology'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link_url',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
