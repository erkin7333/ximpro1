# Generated by Django 4.0.4 on 2022-07-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_staticcontent_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticcontent',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Slug'),
        ),
    ]
