FROM python:3.10-slim

# Prevents Python from writing pyc files to disc and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Use environment variables for Gunicorn configuration with defaults
ENV GUNICORN_TIMEOUT=120
ENV GUNICORN_WORKERS=3
ENV GUNICORN_WORKER_CLASS=sync

CMD gunicorn TinyURL.wsgi:application --bind 0.0.0.0:8000 \
    --timeout ${GUNICORN_TIMEOUT} \
    --workers ${GUNICORN_WORKERS} \
    --worker-class ${GUNICORN_WORKER_CLASS} \
    --log-level info \
    --access-logfile - \
    --error-logfile -