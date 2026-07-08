from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db   
from schemas import DeploymentCreate, DeploymentResponse
from models import DeploymentDB

router = APIRouter(
    prefix="/deployments", 
    tags=["Deployments"]
)

@router.get("", response_model=list[DeploymentResponse])
def get_deployment(db: Session = Depends(get_db)):
    return db.query(DeploymentDB).all()

@router.post("", response_model=DeploymentResponse)
def create_deployment(deployment: DeploymentCreate, db: Session = Depends(get_db)):
    new_deployment = DeploymentDB(
        environment_id=deployment.environment_id,
        version=deployment.version,
        status=deployment.status
    )
    
    db.add(new_deployment)
    db.commit()
    db.refresh(new_deployment)
    
    return new_deployment

@router.delete("/{deployment_id}")
def delete_deployment(deployment_id: int, db: Session = Depends(get_db)):
    deployment = db.query(DeploymentDB).filter(DeploymentDB.id == deployment_id).first()

    db.delete(deployment)
    db.commit()

    return {
        "message": f"Deployment {deployment_id} deleted successfully"
    }

@router.put("/{deployment_id}", response_model=DeploymentResponse)
def update_deployment(deployment_id: int, deployment: DeploymentCreate, db: Session = Depends(get_db)):
    deployment = db.query(DeploymentDB).filter(DeploymentDB.id == deployment_id).first()
    db.update(deployment)
    db.commit()
    db.refresh(deployment)