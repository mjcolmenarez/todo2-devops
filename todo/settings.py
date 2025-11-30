from pathlib import Path
import os   # 👈 add this

BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key – default is dev-only, Azure overrides via environment
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-later")

# Debug – read from env, default True for local dev
DEBUG = os.environ.get("DEBUG", "True") == "True"

# Allowed hosts – comma-separated list from env
raw_hosts = os.environ.get("ALLOWED_HOSTS", "")
ALLOWED_HOSTS = [h.strip() for h in raw_hosts.split(",") if h.strip()]

#Apps we're using. "tasks" is the home-grown here 
#If something doesn't exists you check it here
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tasks",
]

#Security, sessions, csrf, etc. Like the security when building features
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

#HTML brain. Django looks here to figure out how to render pages
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

#Here's where the data is (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

#CSS, images, etc. Django serves them for us
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
