# Generated by Django 4.0.4 on 2022-07-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_projectstranslation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
    ]
