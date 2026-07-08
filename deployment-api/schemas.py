from pydantic import BaseModel
from datetime import datetime

class ProjectCreate(BaseModel):
    name: str
    description: str

class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        from_attributes = True

class EnvironmentCreate(BaseModel):
    project_id: int
    name: str

class EnvironmentResponse(EnvironmentCreate):
    id: int

    class Config:
        from_attributes = True

class DeploymentCreate(BaseModel):
    environment_id: int
    version: str
    status: str
    
class DeploymentUpdate(BaseModel):
    version: str
    status: str

class DeploymentResponse(DeploymentCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True





