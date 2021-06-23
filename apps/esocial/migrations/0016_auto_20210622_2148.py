# Generated by Django 3.2.4 on 2021-06-22 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0015_auto_20210621_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='evento',
            field=models.CharField(choices=[('s1000', 'S-1000 - Informações do Empregador/Contribuinte/Órgão Público'), ('s1005', 'S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos'), ('s1010', 'S-1010 - Tabela de Rubricas'), ('s1020', 'S-1020 - Tabela de Lotações Tributárias'), ('s1070', 'S-1070 - Tabela de Processos Administrativos/Judiciais'), ('s1200', 'S-1200 - Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social'), ('s1202', 'S-1202 - Remuneração de Servidor vinculado ao Regime Próprio de Previd. Social'), ('s1207', 'S-1207 - Benefícios - Entes Públicos'), ('s1210', 'S-1210 - Pagamentos de Rendimentos do Trabalho'), ('s1260', 'S-1260 - Comercialização da Produção Rural Pessoa Física'), ('s1270', 'S-1270 - Contratação de Trabalhadores Avulsos Não Portuários'), ('s1280', 'S-1280 - Informações Complementares aos Eventos Periódicos'), ('s1298', 'S-1298 - Reabertura dos Eventos Periódicos'), ('s1299', 'S-1299 - Fechamento dos Eventos Periódicos'), ('s2198', 'S-2190 - Registro Preliminar de Trabalhador'), ('s2200', 'S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador'), ('s2205', 'S-2205 - Alteração de Dados Cadastrais do Trabalhador'), ('s2206', 'S-2206 - Alteração de Contrato de Trabalho/Relação Estatutária'), ('s2210', 'S-2210 - Comunicação de Acidente de Trabalho'), ('s2020', 'S-2220 - Monitoramento da Saúde do Trabalhador'), ('s2230', 'S-2230 - Afastamento Temporário'), ('s2231', 'S-2231 - Cessão/Exercício em Outro Órgão'), ('s2240', 'S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos'), ('s2298', 'S-2298 - Reintegração/Outros Provimentos'), ('s2299', 'S-2299 - Desligamento'), ('s2300', 'S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início'), ('s2306', 'S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual'), ('s2399', 'S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término'), ('s2400', 'S-2400 - Cadastro de Beneficiário - Entes Públicos - Início'), ('s2405', 'S-2405 - Cadastro de Beneficiário - Entes Públicos - Alteração'), ('s2410', 'S-2410 - Cadastro de Benefício - Entes Públicos - Início'), ('s2416', 'S-2416 - Cadastro de Benefício - Entes Públicos - Alteração'), ('s2418', 'S-2418 - Reativação de Benefício - Entes Públicos'), ('s2428', 'S-2420 - Cadastro de Benefício - Entes Públicos - Término'), ('s3000', 'S-3000 - Exclusão de Eventos')], max_length=20, verbose_name='Evento'),
        ),
        migrations.AlterField(
            model_name='eventoshistorico',
            name='evento',
            field=models.CharField(choices=[('s1000', 'S-1000 - Informações do Empregador/Contribuinte/Órgão Público'), ('s1005', 'S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos'), ('s1010', 'S-1010 - Tabela de Rubricas'), ('s1020', 'S-1020 - Tabela de Lotações Tributárias'), ('s1070', 'S-1070 - Tabela de Processos Administrativos/Judiciais'), ('s1200', 'S-1200 - Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social'), ('s1202', 'S-1202 - Remuneração de Servidor vinculado ao Regime Próprio de Previd. Social'), ('s1207', 'S-1207 - Benefícios - Entes Públicos'), ('s1210', 'S-1210 - Pagamentos de Rendimentos do Trabalho'), ('s1260', 'S-1260 - Comercialização da Produção Rural Pessoa Física'), ('s1270', 'S-1270 - Contratação de Trabalhadores Avulsos Não Portuários'), ('s1280', 'S-1280 - Informações Complementares aos Eventos Periódicos'), ('s1298', 'S-1298 - Reabertura dos Eventos Periódicos'), ('s1299', 'S-1299 - Fechamento dos Eventos Periódicos'), ('s2198', 'S-2190 - Registro Preliminar de Trabalhador'), ('s2200', 'S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador'), ('s2205', 'S-2205 - Alteração de Dados Cadastrais do Trabalhador'), ('s2206', 'S-2206 - Alteração de Contrato de Trabalho/Relação Estatutária'), ('s2210', 'S-2210 - Comunicação de Acidente de Trabalho'), ('s2020', 'S-2220 - Monitoramento da Saúde do Trabalhador'), ('s2230', 'S-2230 - Afastamento Temporário'), ('s2231', 'S-2231 - Cessão/Exercício em Outro Órgão'), ('s2240', 'S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos'), ('s2298', 'S-2298 - Reintegração/Outros Provimentos'), ('s2299', 'S-2299 - Desligamento'), ('s2300', 'S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início'), ('s2306', 'S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual'), ('s2399', 'S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término'), ('s2400', 'S-2400 - Cadastro de Beneficiário - Entes Públicos - Início'), ('s2405', 'S-2405 - Cadastro de Beneficiário - Entes Públicos - Alteração'), ('s2410', 'S-2410 - Cadastro de Benefício - Entes Públicos - Início'), ('s2416', 'S-2416 - Cadastro de Benefício - Entes Públicos - Alteração'), ('s2418', 'S-2418 - Reativação de Benefício - Entes Públicos'), ('s2428', 'S-2420 - Cadastro de Benefício - Entes Públicos - Término'), ('s3000', 'S-3000 - Exclusão de Eventos')], max_length=20, verbose_name='Evento'),
        ),
    ]
