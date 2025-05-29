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

CMD [ "gunicorn", "TinyURL.wsgi:application", "--bind", "0.0.0.0:8000"]