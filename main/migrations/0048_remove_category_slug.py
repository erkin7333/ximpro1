# Generated by Django 3.2 on 2022-07-28 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20220728_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
