# Generated by Django 4.2.7 on 2023-11-09 10:56

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('name', models.CharField(max_length=300, verbose_name='İsim')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/what_we_do/editions', verbose_name='Resim')),
                ('writer', models.CharField(max_length=300, verbose_name='Yazar')),
                ('year', models.SmallIntegerField(verbose_name='Yıl')),
                ('publisher', models.CharField(blank=True, max_length=300, null=True, verbose_name='Yayın Evi')),
            ],
            options={
                'verbose_name_plural': 'Yayınlar',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='img/what_we_do/reports', verbose_name='Ek Dosya')),
            ],
            options={
                'verbose_name_plural': 'Projeler',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='img/what_we_do/reports', verbose_name='Ek Dosya')),
            ],
            options={
                'verbose_name_plural': 'Raporlar',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ReportsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=300, verbose_name='İsim')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='what_we_do.reports')),
            ],
            options={
                'verbose_name': 'reports Translation',
                'db_table': 'what_we_do_reports_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProjectsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=300, verbose_name='İsim')),
                ('description', models.CharField(max_length=300, verbose_name='Açıklama')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='what_we_do.projects')),
            ],
            options={
                'verbose_name': 'projects Translation',
                'db_table': 'what_we_do_projects_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
