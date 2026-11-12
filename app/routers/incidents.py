from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Incident
from ..schemas import IncidentCreate, IncidentResponse


router = APIRouter(
    prefix="/incidents",
    tags = ["Incidents"]
)

@router.post("/", response_model=IncidentResponse, status_code=201)
def create_incident(
        incident: IncidentCreate ,
        db: Session = Depends(get_db)
):
    #mistake
    # data = {
    #     "title" : incident.title,
    #     "description" : incident.description,
    #     "severity" : incident.severity,
    #     "status" : incident.status
    #         }
    
    db_incident = Incident(**incident.model_dump())
    db.add(db_incident)
    db.commit()
    db.refresh()

    return db_incident