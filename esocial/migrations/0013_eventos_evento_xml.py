# Generated by Django 2.2.13 on 2020-12-14 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0012_auto_20201110_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='evento_xml',
            field=models.TextField(blank=True, null=True, verbose_name='XML'),
        ),
    ]
