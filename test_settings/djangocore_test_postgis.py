DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'djangotests_gis',
        'USER': 'django',
        'HOST': 'localhost',
        'PASSWORD': 'secret',
    },
    'other': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'djangotests_gis_other',
        'USER': 'django',
        'HOST': 'localhost',
        'PASSWORD': 'secret',
    },
}

SECRET_KEY = 'django_tests_secret_key'
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)