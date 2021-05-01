# Generated by Django 2.2.13 on 2020-11-02 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0007_auto_20201101_0925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transmissoreventos',
            options={'verbose_name': 'Transmissor do ', 'verbose_name_plural': 'Transmissor do '},
        ),
        migrations.AlterField(
            model_name='eventos',
            name='transmissor_eventos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='eventos_transmissor_eventos', to='esocial.TransmissorEventos'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='transmissor_eventos_error',
            field=models.ManyToManyField(blank=True, related_name='eventos_transmissor_eventos_erros', to='esocial.TransmissorEventos'),
        ),
        migrations.AlterField(
            model_name='importacaoarquivoseventos',
            name='importacao_arquivos',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='importacaoarquivoseventos_importacao_arquivos', to='esocial.ImportacaoArquivos'),
        ),
        migrations.AlterField(
            model_name='transmissor',
            name='certificado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transmissor_certificado', to='esocial.Certificados'),
        ),
        migrations.AlterField(
            model_name='transmissoreventos',
            name='resposta_codigo',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (101, '101 - Lote Aguardando Processamento'), (201, '201 - Lote Processado com Sucesso'), (202, '202 - Lote Processado com Advertências'), (301, '301 - Erro Servidor '), (401, '401 - Lote Incorreto - Erro preenchimento'), (402, '402 - Lote Incorreto - schema Inválido'), (403, '403 - Lote Incorreto - Versão do Schema não permitida'), (404, '404 - Lote Incorreto - Erro Certificado'), (405, '405 - Lote Incorreto - Lote nulo ou vazio'), (501, '501 - Solicitação de Consulta Incorreta - Erro Preenchimento'), (502, '502 - Solicitação de Consulta Incorreta - Schema Inválido.'), (503, '503 - Solicitação de Consulta Incorreta - Versão do Schema Não Permitida.'), (504, '504 - Solicitação de Consulta Incorreta - Erro Certificado.'), (505, '505 - Solicitação de Consulta Incorreta - Consulta nula ou vazia.')], null=True),
        ),
        migrations.AlterField(
            model_name='transmissoreventos',
            name='transmissor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transmissoreventos_transmissor', to='esocial.Transmissor'),
        ),
    ]
