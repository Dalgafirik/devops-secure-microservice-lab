# DevOps Secure Microservice Lab

This repository is a hands-on DevOps learning project.

The purpose of this project is to build a small but realistic microservice and improve it step by step using DevOps practices.

## Current State

- Simple Flask-based microservice
- Configuration managed via environment variables
- Dockerized application
- Docker Compose for local orchestration

## Tech Stack

- Python (Flask)
- Docker
- Docker Compose

## Project Structure

- `service/` → application source code and Dockerfile
- `docker-compose.yml` → service orchestration
- `.env` → environment configuration (not committed)
- `.gitignore` → ignored files

## Run Locally

```bash
docker compose up -d --build
