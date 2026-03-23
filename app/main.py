from fastapi import FastAPI

app = FastAPI(
    title="Git Workflow Demo Clean",
    description="A simple API used to demonstrate a professional Git workflow.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {
        "message": "Git Workflow Demo Clean API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "git-workflow-demo-clean",
        "version": "0.1.0",
        "environment": "production"
    }

@app.post("/auth/login")
def login():
    return {
        "message": "User login endpoint",
        "success": True
    }


@app.post("/auth/logout")
def logout():
    return {
        "message": "User logout endpoint",
        "success": True
    }


@app.get("/profile")
def get_profile():
    return {
        "id": 1,
        "username": "system_user",
        "email": "system@example.com",
        "role": "admin"
    }

@app.put("/profile")
def update_profile():
    return {"message": "Profile updated successfully"}