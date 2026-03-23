from fastapi import FastAPI

app = FastAPI(
    title="Git Workflow Demo Clean",
    description="A simple API used to demonstrate a professional Git workflow.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Git Workflow Demo Clean API"}


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "git-workflow-demo-clean",
        "version": "0.1.0"
    }