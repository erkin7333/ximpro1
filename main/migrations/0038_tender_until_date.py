# Generated by Django 4.0.4 on 2022-07-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_tender_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='until_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Until Date'),
        ),
    ]
