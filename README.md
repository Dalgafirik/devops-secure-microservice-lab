# DevOps Secure Microservice Lab

This repository is a hands-on DevOps learning project that evolves step by step
towards a production-ready system.

The project simulates a real-world pizza shop backend and focuses on containerization,
service health, and operational readiness rather than business complexity.

---

## Current Architecture

- Java Spring Boot backend service
- Dockerized using multi-stage builds
- Docker Compose for local orchestration
- Health checks enabled for container monitoring
- Legacy Flask service retired as part of a controlled migration

---

## Services

### Pizza Backend
- Technology: Java 17, Spring Boot
- Port: 8080
- Health Endpoint: `/health`
- Container health monitored via Docker healthcheck

---

## Tech Stack

- Java 17
- Spring Boot
- Maven
- Docker
- Docker Compose

---

## Project Structure


```text
devops-secure-microservice-lab/
├── backend/
│   └── pizza-service/
│       ├── Dockerfile        # Container definition for the service
│       ├── pom.xml           # Maven configuration
│       └── src/              # Application source code
├── docker-compose.yml        # Multi-container orchestration
├── README.md                 # Project documentation
└── service/                  # Legacy Flask service (retired)


---

## Running Locally

Build and start the services:

```bash
docker compose up -d --build

Check service health:

curl http://localhost:8080/health

---
##Notes

This project prioritizes DevOps practices such as container lifecycle management,
health monitoring, and controlled service evolution over application feature completeness.
