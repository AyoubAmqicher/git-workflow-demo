# Git Workflow Demo Clean

A small FastAPI project built to demonstrate a professional Git workflow using realistic branching and pull request practices.

## Tech Stack
- Python
- FastAPI
- Uvicorn

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Current Endpoints

- `GET /`
- `GET /health`
- `POST /auth/login`
- `POST /auth/logout`
- `GET /profile` → fetch current user profile with role information
- `PUT /profile` → update user profile

## Purpose 

This repository is designed to simulate a real-world team workflow and provide portfolio proof of Git skills.