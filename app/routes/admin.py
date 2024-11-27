from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.authentications import create_access_token, verify_password
from app.services import get_admin_by_email
from app.db_connector import get_db_session
from app.schemas import AdminLogin

admin_router = APIRouter()

@admin_router.post("/login")
def login_admin(admin_data: AdminLogin, db: Session = Depends(get_db_session)):
    admin = get_admin_by_email(db=db, email=admin_data.email)
    if admin is None or not verify_password(admin_data.password, admin.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # Create and return JWT token
    access_token = create_access_token(data={"sub": admin.email})
    return {"access_token": access_token, "token_type": "bearer"}