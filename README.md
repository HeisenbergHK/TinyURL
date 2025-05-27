# TinyURL - URL Shortener

A clean, efficient URL shortening service built with Django, demonstrating modern backend development best practices and cloud-native deployment.

## Features
- Shorten long URLs into concise, unique links
- Redirect users seamlessly to the original URLs
- Follows Angular commit message conventions for clear history
- Fully Dockerized for environment consistency
- Orchestrated with Kubernetes on Minikube for local testing
- Cloud deployment ready with scalable design

## Tech Stack
- __Backend:__ Python 3, Django
- __Database:__ PostgreSQL (configurable)
- __Containerization:__ Docker
- __Orchestration:__ Kubernetes (Minikube)
- __Version Control:__ Git with Angular commit messages

## Local Development Setup
```
# Clone the repo
git clone https://github.com/yourgithubusername/tinyurl.git
cd tinyurl

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
touch .env
# Edit .env with your database credentials and secret keys

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

## Docker
### Build Docker Image
```
docker build -t yourdockerhubusername/tinyurl:latest .
```

### Run Docker Container
```
docker run -d -p 8000:8000 --env-file .env hassankalantari/tinyurl:latest
```

## Kubernetes (Minikube)

### Start Minikube
```
minikube start
```
### Deploy App
```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
### Access App
```
minikube service tinyurl-service
```

## Commit Message Guidelines
This project follows the [Angular Commit Message Conventions](https://www.conventionalcommits.org/en/v1.0.0/) for clear and consistent commit history, e.g.:
```
feat: add URL shortening endpoint
fix: correct redirect logic for empty URLs
chore: update Dockerfile to use Python 3.10
```

