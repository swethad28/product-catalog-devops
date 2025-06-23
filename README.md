# Product Catalog

A fully containerized and scalable microservice to manage a product catalog, built using FastAPI. This includes Dockerization, Kubernetes deployment, Git versioning, GitHub Actions CI/CD pipeline, and full automation practices used by top tech companies.

---

## Overview

| Task                | Description                                      |
|---------------------|--------------------------------------------------|
| Containerization | Docker multi-stage build, slim image, healthcheck |
| Version Control  | Git tags with v1.0.0, v1.1.0, v2.0.0              |
| Kubernetes       | Deploy on Minikube with Ingress & HPA            |
| CI/CD Automation | GitHub Actions triggered on version tags         |
| Docs             | System design, changelog, and usage              |

---

## Tech Stack

- **Backend:** FastAPI
- **Container:** Docker (multi-stage, Alpine/Slim)
- **Orchestration:** Kubernetes via Minikube
- **Routing:** NGINX Ingress Controller
- **Scaling:** HPA with resource limits
- **CI/CD:** GitHub Actions

---

## API Endpoints

| Endpoint                             | Version | Description |
|--------------------------------------|---------|-------------|
| `/health`                            | v1.0+   | Returns status OK |
| `/products`                          | v1.0+   | Returns product list |
| `/products/search?keyword=...`       | v1.1+   | Search products |
| `/products/search?...&min_price=...&max_price=...` | v2.0+ | Filtered search + errors |

---

## To Run Locally (Docker)

```bash
docker build -t product-catalog:v1.0.0 .
docker run -d -p 8000:8000 product-catalog:v1.0.0

# Test endpoints
curl http://localhost:8000/health
curl http://localhost:8000/products
```
## Deploy on Kubernetes (Minikube)

1. Start minikube
```bash
minikube start
``` 
2. Create Namespaces 
   ```bash
   kubectl create namespace catalog-v1
   kubectl create namespace catalog-v1-1
   kubectl create namespace catalog-v2
   ```

3. Apply Deployment & Services 
```bash
   kubectl apply -f k8s/v1/
   kubectl apply -f k8s/v1.1/
   kubectl apply -f k8s/v2/
```
4. Apply Ingress
```bash
minikube addons enable ingress
kubectl apply -f k8s/ingress.yaml
```
5. Get Minikube IP
```bash
minikube ip
```
Visit:

http://<minikube-ip>/v1/health
http://<minikube-ip>/v1.1/products/search?keyword=shoes
http://<minikube-ip>/v2/products/search?min_price=500&max_price=4000

## CI/CD with GitHub Actions
```bash
git tag v1.0.0
git push origin v1.0.0
```
GitHub Secrets Required:
| Secret Name        | Description                     |
| ------------------ | ------------------------------- |
| `DOCKER_USERNAME`  | Docker Hub username             |
| `DOCKER_PASSWORD`  | Docker Hub token/password       |
| `KUBE_CONFIG_DATA` | Base64 of your `~/.kube/config` |

To get kubeconfig secret:
```bash
cat ~/.kube/config | base64
```

