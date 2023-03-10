# Generated by Django 4.0.4 on 2022-07-22 10:41

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_remove_services_customer_projects_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=False, max_length=200, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/projects')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ['order'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NewsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.news')),
            ],
            options={
                'verbose_name': 'News Translation',
                'db_table': 'main_news_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='servicestranslation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='servicestranslation',
            name='master',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.DeleteModel(
            name='ServicesTranslation',
        ),
    ]
