from sqlalchemy.orm import Session
from app import models
from app.schemas import OrganizationCreate
from app.authentications import hash_password

def create_organization(db: Session, org_data: OrganizationCreate):
    # Create organization entry
    org = models.Organization(name=org_data.organization_name, db_name=f"{org_data.organization_name}_db")
    db.add(org)
    db.commit()
    db.refresh(org)

    # Create admin for organization
    hashed_password = hash_password(org_data.password)
    admin = models.Admin(email=org_data.email, hashed_password=hashed_password, organization_id=org.id)
    db.add(admin)
    db.commit()
    db.refresh(admin)

    return org

def get_organization_by_name(db: Session, organization_name: str):
    return db.query(models.Organization).filter(models.Organization.name == organization_name).first()

def get_admin_by_email(db: Session, email: str):
    return db.query(models.Admin).filter(models.Admin.email == email).first()
