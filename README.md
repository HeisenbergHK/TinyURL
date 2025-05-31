# 🔗 TinyURL – Scalable URL Shortener Service

**TinyURL** is a professional-grade URL shortening service built with Django, PostgreSQL, Docker, and Kubernetes. It demonstrates modern backend engineering and DevOps practices, including CI/CD pipelines, container orchestration, and cloud-native architecture.

> ✅ Clean codebase  
> ✅ Production-ready Docker setup  
> ✅ Kubernetes manifests included  
> ✅ GitHub Actions CI/CD pipeline  

---

## 🚀 Key Features

- 🔗 Shorten long URLs into concise, shareable links
- 📱 Mobile-friendly, responsive UI
- 🐳 Multi-environment support: Local, Docker, Kubernetes
- ☁️ Cloud-native configuration and secret management
- 🔄 Fully integrated CI/CD pipeline with GitHub Actions

---

## 🛠️ Tech Stack

| Layer         | Tools                          |
|---------------|--------------------------------|
| Backend       | Python 3.11, Django             |
| Database      | PostgreSQL 15                  |
| Web Server    | Gunicorn                        |
| Containerization | Docker                      |
| Orchestration | Kubernetes (Minikube)          |
| CI/CD         | GitHub Actions                 |

---

## 🏗️ Architecture Overview

The app follows a clean microservice-style separation:

- **Django** – Handles all business logic and routing
- **PostgreSQL** – Stores all URL mappings securely
- **Docker & Kubernetes** – Enables portability, scalability, and infrastructure as code
- **Environment Config** – .env files, secrets, and ConfigMaps for each environment

---

## 🚀 Deployment Options

### 1️⃣ Local Development

```bash
# Clone the repo
git clone https://github.com/hassankalantari/tiny-url.git
cd tiny-url

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cat > .env << EOL
POSTGRES_DB=tinyurl
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
SECRET_KEY=your_secret_key_here
DEBUG=True
EOL

# Run migrations and start server
python manage.py migrate
python manage.py runserver
```

### 2️⃣ Docker Compose
```bash
# Clone the repo
git clone https://github.com/hassankalantari/tiny-url.git
cd tiny-url

# Create environment file
cat > .env << EOL
POSTGRES_DB=tinyurl
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
SECRET_KEY=your_secret_key_here
DEBUG=False
EOL

# Start services
docker-compose up -d

# Access at http://localhost:8000
```

### 3️⃣ Kubernetes (Minikube)
```bash
# Start Minikube
minikube start

# Apply namespace and configs
kubectl apply -f K8s/namespace.yaml
kubectl apply -f K8s/ConfigMap.yml
kubectl apply -f K8s/django-secrets.yml
kubectl apply -f K8s/postgresql-secrets.yaml

# Deploy PostgreSQL
kubectl apply -f K8s/postgresql-pvc.yaml
kubectl apply -f K8s/postgresql-deployment.yaml
kubectl apply -f K8s/postgresql-service.yaml

# Deploy Django app
kubectl apply -f K8s/django-deployment.yaml
kubectl apply -f K8s/django-service.yaml
kubectl apply -f K8s/django-ingress.yaml

# Access the app
minikube service django-service -n tiny-url-namespace
```

## 🔄 CI/CD with GitHub Actions
This project includes two automated workflows:

### ✅ Continuous Integration
Triggered on push and pull requests:
- Set up Python and PostgreSQL
- Run Django unit tests
- Validate Gunicorn setup

### 🚀 Continuous Deployment

Triggered on Git tags (v*.*.*):
- Build Docker image
- Push to Docker Hub with latest and version tags

## 📁 Project Structure
```
tiny-url/
├── .github/workflows/       # CI/CD pipelines
├── K8s/                     # Kubernetes manifests
├── TinyURL/                 # Django project config
├── URLApp/                  # App logic and views
├── docker-compose.yml       # Docker Compose config
├── Dockerfile               # Docker image definition
└── requirements.txt         # Python dependencies
```

### 🧪 Running Tests
```bash
# Local testing
python manage.py test

# Docker Compose
docker-compose run web python manage.py test
```

## 🤝 Contributing
Contributions are welcome!
1.	Fork the repo
2.	Create your feature branch: git checkout -b feature/amazing-feature
3.	Commit with Conventional Commits
4.	Push your branch: git push origin feature/amazing-feature
5.	Open a Pull Request 🚀
---
#### Built with ❤️ by [Hassan Kalantari](https://github.com/hassankalantari)
