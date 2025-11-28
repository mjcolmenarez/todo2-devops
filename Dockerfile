# Dockerfile

FROM python:3.12-slim

# Don't write .pyc files, and unbuffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (you probably don't need many, but keep pip working)
RUN apt-get update && apt-get install -y \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Django settings module (Azure also sets this with env vars)
ENV DJANGO_SETTINGS_MODULE=todo.settings

# Collect static files if you have any (won't fail the build if not configured)
RUN python manage.py collectstatic --noinput || true

# Expose the port your app listens on
EXPOSE 8000

# Start gunicorn (Django via WSGI)
CMD ["gunicorn", "todo.wsgi:application", "--bind", "0.0.0.0:8000"]
