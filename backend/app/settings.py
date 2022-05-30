import os
from .django_settings import *

INSTALLED_APPS += [
    'shops',
    'rest_framework',
    'drf_yasg',
]
LANGUAGE_CODE = 'ru-ru'


LOGGING_LEVEL = 'DEBUG' if DEBUG else 'INFO'
LOG_FORMATTING = 'detail' if DEBUG else 'simple'
LOGS_PATH = os.path.join(BASE_DIR, 'logs/')
if not os.path.isdir(LOGS_PATH):
    os.makedirs(LOGS_PATH)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detail': {
            'format': '%(levelname)s | %(asctime)s | %(module)s | line %(lineno)s | %(message)s'
        },
        'simple': {
            'format': '%(levelname)s | %(asctime)s | %(message)s'
        },
    },
    'handlers': {
        'meet': {
            'level': LOGGING_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_PATH, 'meet.log'),
            'formatter': LOG_FORMATTING,
            'maxBytes': 2e+7,
            'backupCount': 10,
        },

    },
    'loggers': {
        'meet': {
            'handlers': [
                'meet',
            ],
            'level': LOGGING_LEVEL,
            'propagate': False
        },

    },
}
