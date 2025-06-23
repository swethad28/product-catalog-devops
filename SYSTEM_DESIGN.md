# System Design – Product Catalog Microservice (DevOps Assignment)

This document explains the architectural decisions made for building, versioning, deploying, and scaling the Product Catalog Microservice.

---

## Architecture Overview

The system consists of a RESTful microservice written in FastAPI, containerized using Docker, and deployed to a Kubernetes cluster (Minikube). It follows best practices in DevOps and software delivery, focusing on modularity, automation, and scalability.

### Microservice Design

- **Framework**: FastAPI
- **Functionality**:
  - `/health` – Health check endpoint
  - `/products` – Returns a sample product list
  - `/products/search` – Keyword and price-filtered search (v1.1+, v2.0)
- **Stateless design** to allow easy scaling and fault tolerance

---

## Docker Architecture

- **Multi-stage Dockerfile** used to:
  - Separate build environment from runtime
  - Minimize image size using Alpine-based or slim images
- **Healthcheck** included in the Dockerfile for monitoring
- **Secrets and environment variables** managed via `.env` file or Docker runtime args

---

## Kubernetes Architecture

- **Cluster**: Minikube
- **Namespaces**: Each version of the microservice deployed to a separate namespace
  - `catalog-v1`
  - `catalog-v1-1`
  - `catalog-v2`
- **Deployments**: Each version has its own deployment and service
- **Ingress Controller**: NGINX, configured to route traffic to different versions:
  - `/v1` → catalog-v1
  - `/v1.1` → catalog-v1-1
  - `/v2` → catalog-v2
- **HPA (Horizontal Pod Autoscaler)**:
  - Configured to auto-scale based on CPU usage
- **Resource Limits**:
  - Each pod is defined with CPU/memory `requests` and `limits` for efficient cluster utilization

---

## CI/CD Architecture (GitHub Actions)

- **Trigger**: Git tag push (`v1.0.0`, `v1.1.0`, `v2.0.0`)
- **Steps**:
  1. Checkout code
  2. Build Docker image tagged with version
  3. Push image to Docker Hub
  4. Deploy to corresponding namespace using `kubectl`
  5. Run a health check post-deployment
- **Secrets Managed in GitHub Actions**:
  - `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `KUBE_CONFIG_DATA`

---

## Security Considerations

- `.env` file used to handle local development secrets
- CI/CD access credentials stored securely in GitHub Secrets
- No hardcoded secrets in code or Dockerfiles

---

## Observability

- `/health` endpoint used for liveliness checks
- Kubernetes logs accessible using `kubectl logs`
- `kubectl rollout status` used in CI/CD for deploy

---
