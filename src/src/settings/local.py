from .base import *             # noqa
import sys
import logging.config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)

INTERNAL_IPS = ['127.0.0.1']

# Django Debug Toolbar
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Log everything to the logs directory at the top
LOGFILE_ROOT = os.path.join(BASE_DIR, 'logs')