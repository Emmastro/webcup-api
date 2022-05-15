import io
import os
from urllib.parse import urlparse

import environ

# Import the original settings from each template
from .basesettings import *

# Load the settings from the environment variable
env = environ.Env()


# check if file exist
if os.path.exists('.env'):
    env.read_env('.env')
else:
    env.read_env(io.StringIO(os.environ.get("APPLICATION_SETTINGS", None)))

# Setting this value from django-environ
#print(env.dict())
#print("Env", help(env))

SECRET_KEY = env("SECRET_KEY")

# If defined, add service URL to Django security settings
CLOUDRUN_SERVICE_URL = env("CLOUDRUN_SERVICE_URL", default=None)
if CLOUDRUN_SERVICE_URL:
    ALLOWED_HOSTS = [urlparse(CLOUDRUN_SERVICE_URL).netloc, 'alc-ninjas-app.herokuapp.com', 'localhost:3000']
    CSRF_TRUSTED_ORIGINS = [
        CLOUDRUN_SERVICE_URL,
        'https://alc-ninjas-app.herokuapp.com',
        'http://localhost:3000',
        'https://django-cloudrun-lsmeeds47a-uc.a.run.app']
else:
    ALLOWED_HOSTS = ['*'] # ['https://alc-ninjas-app.herokuapp.com', 'http://localhost:3000', 'localhost', 'http://localhost']

# Default false. True allows default landing pages to be visible
DEBUG = env("DEBUG", default=False)

HOST = env("HOST", default=None)

# Set this value from django-environ
if HOST!="local":
    DATABASES = {"default": env.db()}
    # TODO: set password on secret manager
    DATABASES['default']['PASSWORD'] = env("DATABASE_PASSWORD")
    # Define static storage via django-storages[google]
    GS_BUCKET_NAME = env("GS_BUCKET_NAME")
    STATICFILES_DIRS = []
    DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    GS_DEFAULT_ACL = "publicRead"


# Change database settings if using the Cloud SQL Auth Proxy
if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
    DATABASES["default"]["HOST"] = "127.0.0.1"
    DATABASES["default"]["PORT"] = 5432

if "webcup" not in INSTALLED_APPS:
     INSTALLED_APPS += ["webcup"] # for custom data migration

