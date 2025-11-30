# To-do list Web Application
---

## 1. Overview

This project is a small task manager built to practise DevOps concepts:

- Django app with task CRUD, list view and Kanban-style board
- Automated tests and coverage using `pytest` / `pytest-django`
- CI/CD pipeline with GitHub Actions
- Deployment to Azure Web App (Linux, Python stack)
- Basic monitoring via `/health` and `/metrics` endpoints

---

## 2. Features

**User-facing**

- Create, update and delete tasks
- Fields: title, description, due date, priority, status
- Main list view with basic stats
- Kanban view grouped by status (To do / Doing / Done)
- Export all tasks as CSV
- Dark themed UI using `static/css/styles.css`

**DevOps / Infra**

- `pytest` test suite with coverage threshold
- GitHub Actions workflow for CI/CD
- Dockerfile for container image builds
- Azure Web App deployment with startup command
- `/health` endpoint for liveness checks
- `/metrics` endpoint exposing simple JSON metrics

---

## 3. Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (development + small deployments)
- **Frontend:** Django templates + custom CSS
- **CI/CD:** GitHub Actions
- **Runtime:** Azure Web App for Linux (Python)
- **Container (optional):** Docker + Gunicorn

---

## 4. Getting Started (Local Development)
### 4.1 Prerequisites 
- Python 3.12+ (3.13 also works locally)
- git
- (Optional) Docker

### 4.2 Clone the Repository 
- git clone https://github.com/mjcolmenarez/todo2-devops.git

### 4.3 Create and activate a virtualenv
python -m venv venv
- Windows
venv\Scripts\activate
- macOS / Linux
source venv/bin/activate

### 4.4 Install dependencies 
pip install --upgrade pip
pip install -r requirements.txt

### 4.5 Set environment variables (local)
For local development you can either export these or use a .env file + python-dotenv:
export DJANGO_DEBUG=1
export SECRET_KEY="dev-only-change-later"
export ALLOWED_HOSTS="localhost,127.0.0.1"
- optional, for CSRF in browsers
export CSRF_TRUSTED_ORIGINS="http://localhost:8000"

### 4.6 Apply database migrations and Run
python manage.py migrate
python manage.py runserver

Open the app at:
http://127.0.0.1:8000/

## 5. Running Tests & Coverage
The project uses pytest, pytest-django and pytest-cov.

From the project root (with the virtualenv active):
pytest

To see coverage information:
pytest --cov=tasks --cov=todo --cov-report=term-missing

The CI pipeline enforces a minimum coverage threshold (e.g. --cov-fail-under=70), so if coverage falls below that, the build fails.

## 6. CI/CD Pipeline (GitHub Actions)
The CI/CD workflow lives at .github/workflows/ci-cd.yml.

At a high level it:

1. Triggers on pushes and pull requests to main.
2. Checks out the repository.
3. Sets up Python and installs requirements.
4. Runs tests with coverage and enforces a minimum coverage percentage.
5. Builds a Docker image (to validate the Dockerfile).
6. Deploys the app to Azure Web App using the azure/webapps-deploy action.

Secrets required in the GitHub repo (names may vary depending on your setup):
- AZURE_WEBAPP_PUBLISH_PROFILE – publish profile XML for the target Web App.

## 7. Azure Deployment
The application is deployed to an Azure Web App (Linux, Python runtime).

Key points:
- Runtime: Python (Linux)
- Startup command (App Service → Configuration → General settings):
python manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 todo.wsgi:application

App Settings / Environment variables:
SECRET_KEY – non-default Django secret key.
DJANGO_DEBUG – set to 0 in production.
ALLOWED_HOSTS – include your Azure hostname, e.g.
your-app-name.azurewebsites.net
CSRF_TRUSTED_ORIGINS – e.g.
https://your-app-name.azurewebsites.net

After deployment, your app will be accessible at:
mjtodo2-codewebapp-e4c2grfvgsgwcjbh.westeurope-01.azurewebsites.net 

## 8. Health & Monitoring 
Two main endpoints are provided:
- /health
    - Simple liveness endpoint returning HTTP 200 when the app is running.
    - Can be used by Azure Health Check.

- /metrics
    - Returns JSON with basic runtime metrics, e.g.:
        - Total requests handled
        - Counts by status code group (2xx, 4xx, 5xx)
        - Last request duration in ms
    - Backed by a small custom middleware.

In Azure, the Log Stream can be used to inspect startup logs (migrations, Gunicorn) and application errors. Combining logs with /health and /metrics makes debugging much easier.
