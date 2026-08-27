from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Sample DevSecOps Microservice")
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"status": "online", "message": "Operational API v2 - GitOps Rocks!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}