from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db_connector import Base

# Organization model
class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    db_name = Column(String, index=True)

    admins = relationship("Admin", back_populates="organization")

# Admin model (for login authentication)
class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    organization_id = Column(Integer, ForeignKey("organizations.id"))

    organization = relationship("Organization", back_populates="admins")
