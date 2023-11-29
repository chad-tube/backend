import os
from .base import *
import dj_database_url

import environ

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR.parent.parent, ".env"))


POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
EXTERNAL_DATABASE_URL = env("EXTERNAL_DATABASE_URL")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
DATABASES = {"default": dj_database_url.parse(EXTERNAL_DATABASE_URL)}
