# Generated by Django 4.2.7 on 2023-12-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_alter_sitesettings_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon'),
        ),
    ]
