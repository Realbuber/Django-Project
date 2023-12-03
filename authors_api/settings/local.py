from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="QtkBH7ssFM8XzRhZpIGvDHYmv_Ko-D1KLTneqpUEf4BNRFAbRtc",
                 )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRD_TRUSTED_ORIGINS = ["http://localhost:8080"]


