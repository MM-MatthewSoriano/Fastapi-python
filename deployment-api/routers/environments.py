from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db   
from schemas import EnvironmentCreate, EnvironmentResponse
from models import EnvironmentDB

router = APIRouter(
    prefix="/environments", 
    tags=["Environments"]
)

@router.post("", response_model=EnvironmentResponse)
def create_environment(environment: EnvironmentCreate, db: Session = Depends(get_db)):
    new_environment = EnvironmentDB(
        name=environment.name,
        project_id=environment.project_id
    )
    
    db.add(new_environment)
    db.commit()
    db.refresh(new_environment)
    
    return new_environment

@router.get("", response_model=list[EnvironmentResponse])
def get_environment(db: Session = Depends(get_db)):
    return db.query(EnvironmentDB).all()
