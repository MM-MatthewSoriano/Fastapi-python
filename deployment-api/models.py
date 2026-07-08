from datetime import datetime
from sqlalchemy import Column,Integer,String, DateTime, ForeignKey
from database import Base

class ProjectDB(Base):
    __tablename__ = "projects"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    description = Column(String)

class EnvironmentDB(Base):
    __tablename__ = "environments"
    id = Column(Integer,primary_key=True,index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    name = Column(String, nullable=False)

class DeploymentDB(Base):
    __tablename__ = "deployments"
    id = Column(Integer, primary_key=True,index=True)
    environment_id = Column(Integer, ForeignKey("environments.id"))
    version =  Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
