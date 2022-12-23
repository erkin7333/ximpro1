# Generated by Django 3.2 on 2022-08-02 09:42

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_auto_20220728_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('file', models.FileField(upload_to='pdf/')),
            ],
            options={
                'verbose_name': 'Pdf File',
                'verbose_name_plural': 'Pdf File',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=500, null=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='membership/', verbose_name='image')),
                ('number', models.CharField(max_length=300, verbose_name='Number')),
                ('email', models.CharField(max_length=300, verbose_name='Email')),
                ('adress', models.CharField(max_length=300, verbose_name='Adress')),
            ],
            options={
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Membership',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='staticcontent',
            name='slug',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Slug'),
        ),
        migrations.CreateModel(
            name='MembershipTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('position', models.CharField(max_length=400, verbose_name='Position')),
                ('description', models.TextField(verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.membership')),
            ],
            options={
                'verbose_name': 'Membership Translation',
                'db_table': 'main_membership_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
