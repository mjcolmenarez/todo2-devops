from pathlib import Path
import os

# -----------------------------------------
# Paths
# -----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------
# Security / environment
# -----------------------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-later")

DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

# ALLOWED_HOSTS from env, comma-separated
raw_hosts = os.environ.get("ALLOWED_HOSTS", "")
if raw_hosts:
    ALLOWED_HOSTS = [h.strip() for h in raw_hosts.split(",") if h.strip()]
else:
    # Local default
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# CSRF trusted origins (needed for Azure HTTPS forms)
raw_csrf = os.environ.get("CSRF_TRUSTED_ORIGINS", "")
if raw_csrf:
    CSRF_TRUSTED_ORIGINS = [o.strip() for o in raw_csrf.split(",") if o.strip()]
else:
    CSRF_TRUSTED_ORIGINS = [
        f"https://{h}"
        for h in ALLOWED_HOSTS
        if "localhost" not in h and "127.0.0.1" not in h
    ]

# -----------------------------------------
# Applications
# -----------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tasks",
]

# -----------------------------------------
# Middleware
# -----------------------------------------
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

# -----------------------------------------
# Templates
# -----------------------------------------
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

# -----------------------------------------
# Database (SQLite)
# -----------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -----------------------------------------
# Internationalization
# -----------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -----------------------------------------
# Static files (CSS, JS, images)
# -----------------------------------------
STATIC_URL = "static/"

# Where your project-level static/ folder lives (for dev)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Where collectstatic will put files (for Azure)
STATIC_ROOT = BASE_DIR / "staticfiles"

# -----------------------------------------
# Default primary key field type
# -----------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
