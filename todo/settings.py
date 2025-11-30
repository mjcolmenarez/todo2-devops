# This file is where we keep all the knobs and switches.
# If you tweak something here and save, the app will often do something different right away.

from pathlib import Path
import os

# Base directory of the project (…/todo2-main)
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret sauce used by Django for security stuff.
# In production (Azure) this comes from the environment variable SECRET_KEY.
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-later")

# Great for building: DEBUG=True locally, False in production (Azure).
DEBUG = os.environ.get("DEBUG", "True") == "True"

# Who's allowed to talk to this app.
# In production, set ALLOWED_HOSTS env var to a comma-separated list, e.g.:
# "mjtodo2-codewebapp-xxxx.westeurope-01.azurewebsites.net"
raw_allowed_hosts = os.environ.get("ALLOWED_HOSTS", "")
if raw_allowed_hosts:
    ALLOWED_HOSTS = [h.strip() for h in raw_allowed_hosts.split(",") if h.strip()]
else:
    ALLOWED_HOSTS = []

# If we ever need CSRF_TRUSTED_ORIGINS for HTTPS / custom domains, read from env too
raw_csrf = os.environ.get("CSRF_TRUSTED_ORIGINS", "")
if raw_csrf:
    CSRF_TRUSTED_ORIGINS = [o.strip() for o in raw_csrf.split(",") if o.strip()]

# Apps we're using. "tasks" is the home-grown one here.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tasks",
]

# Security, sessions, csrf, etc. Like the security when building features.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "todo.metrics_middleware.MetricsMiddleware",
]

ROOT_URLCONF = "todo.urls"

# HTML brain. Django looks here to figure out how to render pages.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "todo.wsgi.application"

# Here's where the data is (SQLite).
# For this assignment we keep it simple and use the same DB locally and in Azure.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Internationalisation.
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# CSS, images, etc. Django serves them for us (or via collectstatic in production).
STATIC_URL = "static/"

# Where our local static files live in the repo.
STATICFILES_DIRS = [BASE_DIR / "static"]

# Where `collectstatic` will put files (useful for production / Azure).
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
