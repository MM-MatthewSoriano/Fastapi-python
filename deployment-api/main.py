from fastapi import FastAPI
from database import Base, engine 
from routers import projects, environments, deployments
import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Deployment API is running"}

app.include_router(projects.router)
app.include_router(environments.router)
app.include_router(deployments.router)
