from .base import *  # NOQA

from urllib.parse import urlparse

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "psqlextra.backend",
        "NAME": env.str("POSTGRES_DB"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "HOST": env.str("POSTGRES_HOST"),
        "PORT": 5432,
    }
}

CLOUDRUN_SERVICE_URL = env("CLOUDRUN_SERVICE_URL", default=None)
if CLOUDRUN_SERVICE_URL:
    ALLOWED_HOSTS = [urlparse(CLOUDRUN_SERVICE_URL).netloc]
    CSRF_TRUSTED_ORIGINS = [CLOUDRUN_SERVICE_URL]
    SECURE_SSL_REDIRECT = True
else:
    ALLOWED_HOSTS = []
    CSRF_TRUSTED_ORIGINS = []

CSRF_TRUSTED_ORIGINS += env.list("CSRF_TRUSTED_ORIGINS", default=[])

ALLOWED_HOSTS = (
    [
        "localhost",
        "127.0.0.1",
    ]
    + env.list("ALLOWED_HOSTS", default=[])
    + ALLOWED_HOSTS
)

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Media storage
STORAGES["default"] = {"BACKEND": "storages.backends.gcloud.GoogleCloudStorage"}
GS_BUCKET_NAME = env.str("GS_BUCKET_NAME")
