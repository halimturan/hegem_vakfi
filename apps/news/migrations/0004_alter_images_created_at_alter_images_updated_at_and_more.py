# Generated by Django 4.2.7 on 2023-12-12 13:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_is_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Eklenme'),
        ),
        migrations.AlterField(
            model_name='images',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Düzenlenme'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Eklenme'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Düzenlenme'),
        ),
        migrations.AlterField(
            model_name='newstranslation',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Metin'),
        ),
    ]