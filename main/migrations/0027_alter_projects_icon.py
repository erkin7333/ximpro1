# Generated by Django 4.0.4 on 2022-07-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_projects_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='icon',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
