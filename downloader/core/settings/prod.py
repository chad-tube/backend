import os
from .base import *
import dj_database_url

import environ

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR.parent.parent, ".env"))


EXTERNAL_DATABASE_URL = env("EXTERNAL_DATABASE_URL")

EXTERNAL_REDIS_URL = os.environ.get("EXTERNAL_REDIS_URL")

# Database configuration
DATABASES = {"default": dj_database_url.parse(EXTERNAL_DATABASE_URL)}

# Cache configuration
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": EXTERNAL_REDIS_URL,
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}
