"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    env('ALLOWED_HOSTS'),
]

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# Application definition

INSTALLED_APPS = [
    'adminlteui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'treebeard',
    'constance',
    'constance.backends.database',
    'apps.esocial.apps.esocialConfig',
    'apps.reinf.apps.reinfConfig',
    'apps.contrib.apps.contribConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'constance.context_processors.config',
                'config.context_processors.admin_media',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'Brazil/East'

USE_I18N = True

USE_L10N = True

USE_TZ = False

DECIMAL_SEPARATOR = ','

THOUSAND_SEPARATOR = '.'

USE_THOUSAND_SEPARATOR = True

# Configurações de Versão do Aplicativo

VERSAO_EMENSAGERIA = '1.2.0'
VERSAO_LAYOUT_ESOCIAL = 'v_S_01_00_00'
VERSAO_LAYOUT_REINF = 'v1_04_00'
ESOCIAL_TPAMB = env('ESOCIAL_TPAMB', default='2')
ESOCIAL_PROCEMI = env('ESOCIAL_PROCEMI', default='1')


VERSOES_ESOCIAL = [
    'v_S_01_00_00', ]

VERSOES_REINF = [
    'v1_04_00',
    'v2_00_00']

# caminho dos certificados
CERT_PATH = env('CERT_PATH', default='certificados/')

# Somente no Windows Server
# caminho do CURL
# Necessário baixar o curl para windows no endereço: https://curl.se/windows/
CURL_PATH = env('CURL_PATH', default='')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(env('STATIC_ROOT', default='static'))
STATIC_URL = env('STATIC_URL', default='/static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]

# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, env('MEDIA_ROOT', default='media'))
MEDIA_URL = env('MEDIA_URL', default='/media/')

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAdminUser',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    )
}

# Constance

CONSTANCE_ADDITIONAL_FIELDS = {
    'choices_tp_amb': ['django.forms.fields.ChoiceField', {
        'widget': 'django.forms.Select',
        'choices': (("Produção", "Produção"), ("Produção Restrita", "Produção Restrita"))
    }],
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {

    'SYSTEM_MANUAL_SHOW_IN_MENU': (False,
        'Visualiza manual do sistema no menu.',
        bool),

    'SYSTEM_MANUAL_LINK': ('http://',
         'Link do manual do sistema.',
         str),

    'FILES_PATH': ('/arquivos',
         'Caminho relativo do local aonde serão armazenados os arquivos. Insira "/" no início para definir diretórios absolutos.',
         str),

    'FILTER_BY_USER': (False,
        'Cada usuário pode ver somente os que ele mesmo cadastrou. Os Super-usuários vêem todos os eventos',
        bool),

    'LOGO_IMAGE_IN_LOGIN': (False,
        'Visualiza imagem do logotipo na tela de Login.',
        bool),

    'LOGO_IMAGE': ('', 'Logotipo da empresa', 'image_field'),

    'REPRESENTANTE_NOME': ('EMENSAGERIA',
        'Nome da empresa que está disponibilizando o sistema',
        str),

    'REPRESENTANTE_CENTRAL_SERVICOS': ('Central de Serviços (99) 99999.9999',
        'Contrato da central de serviços',
        str),

    'SYSTEM_TOKEN_SCHEDULE': ('9944b09199c62bcf9418ad846dd0123e4bbdfc6ee4b',
         'Token de autenticação do sistema para acesso aos webservices',
         str),

    'ESOCIAL_VALIDATE_RUN_EVERY_MINS': (10,
        'Tempo entre validações (em minutos) dos eventos do eSocial.',
        int),

    'ESOCIAL_SEND_RUN_EVERY_MINS': (10,
        'Tempo entre envios (em minutos) dos eventos do eSocial.',
        int),

    'ESOCIAL_CONSULT_RUN_EVERY_MINS': (10,
        'Tempo entre consultas (em minutos) dos eventos do eSocial.',
        int),

    'ESOCIAL_LOTE_MIN': (1,
        'Quantidade do mínima do lote do eSocial.',
        int),

    'ESOCIAL_LOTE_MAX': (60,
        'Quantidade do máxima do lote do eSocial.',
        int),

    'ESOCIAL_TIMEOUT': (3600,
        'Timeout do eSocial.',
        int),

    'ESOCIAL_AUTOMATIC_FUNCTIONS_ENABLED': (False,
        'Envio automático do eSocial.',
        bool),

    'ESOCIAL_CA_CERT_PEM_FILE': ('certificado/webservicesproducaorestritaesocialgovbr.crt',
        'Caminho completo do Certificado do SERPRO para o eSocial',
        str),

    'ESOCIAL_TP_AMB': (
        'Produção Restrita',
        'Tipo de ambiente padrão do sistema do eSocial.',
        'choices_tp_amb'),

    'ESOCIAL_FORCE_PRODUCAO_RESTRITA': (True,
        'Força o sistema para envio pelo ambiente produção restrita do eSocial.',
        bool),

    'ESOCIAL_VERIFICAR_PREDECESSAO_ANTES_ENVIO': (False,
        'Ativa a função de verificar predecessão antes dos envios dos eventos do eSocial.',
        bool),

    'IMPORT_FILES_RUN_EVERY_MINS': (10,
        'Tempo de leitura de arquivos importados (em minutos).',
        int),

    'IMPORT_LEN_EVENTS': (10,
        'Quantidade do lote de arquivos de eventos para importação.',
        int),

    'IMPORT_AUTOMATIC_FUNCTIONS_ENABLED': (False,
        'Funções de importação automáticas ativadas.',
        bool),

    'EFDREINF_VALIDADE_RUN_EVERY_MINS': (10,
        'Tempo entre validações (em minutos) dos eventos do EFD-Reinf.',
        int),

    'EFDREINF_SEND_RUN_EVERY_MINS': (10,
        'Tempo entre envios (em minutos) dos eventos do EFD-Reinf.',
        int),

    'EFDREINF_CONSULT_RUN_EVERY_MINS': (10,
        'Tempo entre consultas (em minutos) dos eventos do EFD-Reinf.',
        int),

    'EFDREINF_CA_CERT_PEM_FILE': ('certificados/acserproacfv5.crt',
        'Caminho completo do Certificado do SERPRO para o EFD-Reinf',
        str),

    'EFDREINF_LOTE_MIN': (1,
        'Quantidade do mínima do lote do EFD-Reinf.',
        int),

    'EFDREINF_LOTE_MAX': (60,
        'Quantidade do máxima do lote do EFD-Reinf.',
        int),

    'EFDREINF_TIMEOUT': (3600,
        'Timeout do EFD-Reinf.',
        int),

    'EFDREINF_AUTOMATIC_FUNCTIONS_ENABLED': (False,
        'Envio automático do EFD-Reinf.',
        bool),

    'EFDREINF_TP_AMB': (
        'Produção Restrita',
        'Tipo de ambiente padrão do sistema do EFD-Reinf.',
        'choices_tp_amb'),

    'EFDREINF_FORCE_PRODUCAO_RESTRITA': (True,
        'Força o sistema para envio pelo ambiente produção restrita do EFD-Reinf.',
        bool),

    'EFDREINF_VERIFICAR_PREDECESSAO_ANTES_ENVIO': (False,
        'Ativa a função de verificar predecessão antes dos envios dos eventos do EFD-Reinf.',
        bool),

    'EMAIL_RECUPERACAO_SENHA': ('emensageria@emensageria.com.br',
        'E-mail de recuperação de senha.',
        str),

    'EMAIL_RECUPERACAO_SENHA_ASSUNTO': ('Criação/Recuperação de senha | eMensageria',
        'Assunto padrão do e-mail de recuperação de senha.',
        str),

    'EMAIL_RECUPERACAO_SENHA_MENSAGEM': ('<p>Prezado %(nome)s,<br>Acesse o sistema pelo link <a href="%(endereco)s">eMensageriaPro</a><br>Utilizando o usuário: <strong>%(usuario)s</strong><br>Senha: <strong>%(senha)s</strong><br>E-mail gerado automaticamente pelo sistema eMensageria</p>',
        'Mensagem padrão do e-mail de recuperação de senha.',
        str),

}


ADMINLTE_SETTINGS = {
    # 'demo': True,
    # 'search_form': True,
    # 'skin': 'blue',
    # 'copyright': '<a href="https://github.com/wuyue92tree/django-adminlte-ui/tree/'+version+'">django-adminlte-ui '+version+'</a>',
    # 'navigation_expanded': True,

    # if you are use custom menu, which will not effective below!

    # 'show_apps': ['django_admin_settings', 'auth', 'main'],
    # 'main_navigation_app': 'django_admin_settings',
    'icons': {
        'esocial': {
            'arquivos': 'fa-circle',
            'eventos': 'fa-circle',
        }
    }
}
