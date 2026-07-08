# Deployment API

A RESTful API built with **FastAPI**, **SQLAlchemy**, and **SQLite** for managing software deployment workflows.

The application models a simple deployment pipeline consisting of:

- **Projects** – Applications or services being deployed.
- **Environments** – Deployment targets such as Development, Staging, and Production.
- **Deployments** – Individual deployment records containing version, status, and deployment timestamp.

## Features

- CRUD operations for Projects
- CRUD operations for Environments
- CRUD operations for Deployments
- SQLAlchemy ORM integration
- SQLite database
- Request and response validation using Pydantic
- Interactive API documentation with Swagger UI
- Modular router architecture

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn

## Database Structure

```
Project
│
├── id
├── name
└── description
      │
      ▼
Environment
│
├── id
├── project_id
└── name
      │
      ▼
Deployment
│
├── id
├── environment_id
├── version
├── status
└── created_at
```

## API Endpoints

### Projects

- `POST /projects`
- `GET /projects`
- `PUT /projects/{id}`
- `DELETE /projects/{id}`

### Environments

- `POST /environments`
- `GET /environments`
- `PUT /environments/{id}`
- `DELETE /environments/{id}`

### Deployments

- `POST /deployments`
- `GET /deployments`
- `PUT /deployments/{id}`
- `DELETE /deployments/{id}`

## Purpose

This project was built to practice backend API development using FastAPI, including RESTful API design, database modeling, dependency injection, SQLAlchemy ORM, and Pydantic schema validation while following a modular project structure.

This project was built to practice backend API development using FastAPI, including RESTful API design, database modeling, dependency injection, SQLAlchemy ORM, and Pydantic schema validation while followin moproject structure.
