# Generated by Django 4.2.7 on 2023-11-07 20:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstranslation',
            name='title',
            field=ckeditor.fields.RichTextField(verbose_name='Başlık'),
        ),
    ]