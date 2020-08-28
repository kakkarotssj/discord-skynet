import logging
from logging.config import dictConfig


DB_CONFIGURATIONS = {
    'database': 'skynet',
    'user': 'skynet',
    'password': 'skynet',
    'host': 'localhost',
    'port': 5432
}


LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'custom_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'custom_formatter',
            'level': logging.INFO
        }
    },
    'root': {
        'handlers': ['console'],
        'level': logging.INFO
    }
}
dictConfig(LOG_CONFIG)
