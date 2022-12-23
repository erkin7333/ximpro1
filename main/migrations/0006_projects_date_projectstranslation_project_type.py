# Generated by Django 4.0.4 on 2022-05-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_projects_more_image_projectsimages_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='projectstranslation',
            name='project_type',
            field=models.CharField(blank=True, max_length=200, verbose_name='Project Type'),
        ),
    ]
