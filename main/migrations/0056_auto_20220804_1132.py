# Generated by Django 3.2 on 2022-08-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_auto_20220804_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='events',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Events'),
        ),
        migrations.AddField(
            model_name='news',
            name='news',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='News'),
        ),
    ]
