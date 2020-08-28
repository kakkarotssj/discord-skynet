import logging
from logging.config import dictConfig
import os


DB_CONFIGURATIONS = {
    'database': os.getenv('DATABASE'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT')
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
