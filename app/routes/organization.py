from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import create_organization, get_organization_by_name
from app.db_connector import get_db_session
from app.schemas import OrganizationCreate

org_router = APIRouter()

@org_router.post("/create")
def create_organization(org_data: OrganizationCreate, db: Session = Depends(get_db_session)):
    org = create_organization(db=db, org_data=org_data)
    return {"organization_name": org.name, "db_name": org.db_name}

@org_router.get("/get")
def get_organization(organization_name: str, db: Session = Depends(get_db_session)):
    org = get_organization_by_name(db=db, organization_name=organization_name)
    if org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return {"organization_name": org.name, "db_name": org.db_name}

