from pydantic import BaseModel
from typing import Optional

# Organization schema
class OrganizationCreate(BaseModel):
    email: str
    password: str
    organization_name: str

# Admin login schema
class AdminLogin(BaseModel):
    email: str
    password: str

# Token schema for JWT
class Token(BaseModel):
    access_token: str
    token_type: str
