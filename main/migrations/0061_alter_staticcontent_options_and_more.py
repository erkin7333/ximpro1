# Generated by Django 4.1.4 on 2022-12-24 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_delete_homeimages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staticcontent',
            options={'verbose_name': 'StaticContent'},
        ),
        migrations.AlterModelOptions(
            name='staticcontenttranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'StaticContent Translation'},
        ),
    ]
