from fastapi import FastAPI
from app.routes.admin import admin_router
from app.routes.organization import org_router
from app.db_connector import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(org_router, prefix="/Org", tags=["Organization"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
