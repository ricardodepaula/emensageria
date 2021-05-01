# Generated by Django 2.2.13 on 2020-11-02 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0008_auto_20201102_1011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transmissoreventos',
            options={'verbose_name': 'Transmissor do eSocial', 'verbose_name_plural': 'Transmissor do eSocial'},
        ),
        migrations.RemoveField(
            model_name='transmissor',
            name='data_abertura',
        ),
        migrations.AlterField(
            model_name='transmissor',
            name='certificado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='transmissor_certificado', to='esocial.Certificados'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transmissor',
            name='endereco_completo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='transmissoreventos',
            name='ocorrencias_json',
            field=models.TextField(blank=True, null=True, verbose_name='ocorrencias_json'),
        ),
        migrations.AlterField(
            model_name='transmissoreventos',
            name='retorno_consulta_json',
            field=models.TextField(blank=True, null=True, verbose_name='retorno_consulta_json'),
        ),
        migrations.AlterField(
            model_name='transmissoreventos',
            name='retorno_envio_json',
            field=models.TextField(blank=True, null=True, verbose_name='retorno_envio_json'),
        ),
    ]
