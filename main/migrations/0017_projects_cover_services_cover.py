# Generated by Django 4.0.4 on 2022-05-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_homeimages_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='photos/projects'),
        ),
        migrations.AddField(
            model_name='services',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='photos/projects'),
        ),
    ]