import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações de Desenvolvimento (Mantenha assim por enquanto)
SECRET_KEY = 'django-insecure-chave-provisoria-hugel-manner'
DEBUG = True
ALLOWED_HOSTS = []

# Aplicações instaladas no projeto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Seus aplicativos customizados
    'apps.institucional.apps.InstitucionalConfig',    
    'apps.blog',
    'apps.agenda',
    'apps.parceiros',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    # 🌟 ADICIONADO: Middleware essencial para interceptar o clique nas bandeiras e mudar o idioma
    'django.middleware.locale.LocaleMiddleware', 
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Caminho para a nossa pasta de HTMLs
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core_project.wsgi.application'

# Base de dados padrão do Django (SQLite - cria um arquivo local simples)
# Base de dados padrão do Django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Usando o os.path para cravar o caminho absoluto na raiz do projeto
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Configurações de Idioma e Fuso Horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# 🌟 ADICIONADO: Lista de idiomas suportados no site (bate com as opções do seu base.html)
LANGUAGES = [
    ('pt-br', 'Português'),
    ('de', 'Deutsch'),
    ('en', 'English'),
    ('es', 'Español'),
]

# 🌟 ADICIONADO: Diretório onde ficarão guardados os arquivos de tradução das palavras
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Configuração de Arquivos Estáticos (CSS, JS)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Configuração de Upload de Imagens (Essencial para o Blog e Patrocinadores)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Em desenvolvimento, o e-mail não gasta internet e aparece direto no seu terminal!
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'hugelmannerplattler@gmail.com'  # E-mail que vai enviar
EMAIL_HOST_PASSWORD = 'jodmsdjbvduqrmsf'     # Senha de aplicativo gerada no Google