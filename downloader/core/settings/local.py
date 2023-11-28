import os
from .base import *

import environ

env_file = os.path.join(BASE_DIR.parent.parent, "dev.env")

environ.Env.read_env(env_file)
env = environ.Env()

# DATABASE
POSTGRES_DB = env("POSTGRES_DB")
POSTGRES_USER = env("POSTGRES_USER")
POSTGRES_PASSWORD = env("POSTGRES_PASSWORD")
POSTGRES_HOST = env("POSTGRES_HOST")
POSTGRES_PORT = env("POSTGRES_PORT")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
    }
}

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "backend_cache://0.0.0.0:6405/",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
