# Generated by Django 2.2.2 on 2019-06-29 07:08

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=255, unique=True, verbose_name='Option Name')),
                ('option_value', models.TextField(verbose_name='Option Value')),
                ('create_time', models.DateTimeField(default=timezone.now, verbose_name='CreateTime')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='UpdateTime')),
            ],
            options={
                'verbose_name': 'Options',
                'verbose_name_plural': 'All Options',
            },
        ),
    ]
