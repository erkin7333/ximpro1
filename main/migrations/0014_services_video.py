# Generated by Django 4.0.4 on 2022-05-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_projects_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Video'),
        ),
    ]
