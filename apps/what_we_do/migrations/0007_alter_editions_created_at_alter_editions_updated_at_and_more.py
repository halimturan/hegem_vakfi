# Generated by Django 4.2.7 on 2023-12-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_we_do', '0006_editions_is_publish_projects_is_publish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editions',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Eklenme'),
        ),
        migrations.AlterField(
            model_name='editions',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Düzenlenme'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Eklenme'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Düzenlenme'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Eklenme'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Düzenlenme'),
        ),
    ]
