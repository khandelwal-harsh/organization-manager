from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.schemas import Token

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Secret key and algorithm for JWT
SECRET_KEY = "5a4b3f6c8d9a17d7362b5e2f227a2a1290f6b7b124d7b4f007fd7a7c1ffefc97"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Hashing a password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verifying a password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Create JWT token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
