# Generated by Django 4.2.7 on 2023-11-06 19:34

import ckeditor.fields
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
            name='MainSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('order', models.SmallIntegerField(verbose_name='Sıra')),
                ('image', models.ImageField(upload_to='img/main_slider', verbose_name='Resim')),
                ('image_alignment', models.CharField(choices=[('sag', 'Sağ'), ('sol', 'Sol')], max_length=10, verbose_name='Resim Konumu')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('url', models.CharField(blank=True, max_length=100, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'Ana Slider',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MainSliderTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Metin')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.mainslider')),
            ],
            options={
                'verbose_name': 'main slider Translation',
                'db_table': 'main_mainslider_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
