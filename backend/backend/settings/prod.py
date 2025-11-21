from .base import *

ENV_FILE = ".env.prod"  # specify the environment file for production

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_AGE = 86400  # 1 day in seconds
CSRF_COOKIE_SECURE = True
