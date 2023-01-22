import databases
import enum
import sqlalchemy

import urllib.parse
from decouple import config

from fastapi import FastAPI, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
import jwt
from pydantic import BaseModel, validator
from email_validator import validate_email as validate_e, EmailNotValidError
from typing import Optional
from datetime import datetime, timedelta
from passlib.context import CryptContext

URL_PARSE = urllib.parse.quote_plus(config('DB_PASSWORD'))
DATABASE_URL = f"postgresql://{config('DB_USER')}:{URL_PARSE}@localhost:{config('DB_PORT')}/{config('DATABASE')}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Schema
class ColorEnum(enum.Enum):
    pink = "pink"
    black = "black"
    white = "white"
    yellow = "yellow"


class SizeEnum(enum.Enum):
    xs = "xs"
    s = "s"
    m = "m"
    l = "l"
    xl = "xl"
    xxl = "xxl"


class UserRolesEnum(enum.Enum):
    super_admin = "super admin"
    admin = "admin"
    user = "user"

# Tables of the database
users = sqlalchemy.Table(
            "users",
            metadata,
            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
            sqlalchemy.Column("email", sqlalchemy.String(120), unique=True),
            sqlalchemy.Column("password", sqlalchemy.String(255)),
            sqlalchemy.Column("full_name", sqlalchemy.String(200)),
            sqlalchemy.Column("phone", sqlalchemy.String(13)),
            sqlalchemy.Column("created_at", sqlalchemy.DateTime, nullable=False,
                                server_default=sqlalchemy.func.now()),
            sqlalchemy.Column(
                "last_modified_at",
                sqlalchemy.DateTime,
                nullable=False,
                server_default=sqlalchemy.func.now(),
                onupdate=sqlalchemy.func.now()),
            sqlalchemy.Column("role", sqlalchemy.Enum(UserRolesEnum), nullable=False, 
                                server_default=UserRolesEnum.user.name)
)

clothes = sqlalchemy.Table(
            "clothes",
            metadata,
            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
            sqlalchemy.Column("name", sqlalchemy.String(120)),
            sqlalchemy.Column("color", sqlalchemy.Enum(ColorEnum), nullable=False),
            sqlalchemy.Column("size", sqlalchemy.Enum(SizeEnum), nullable=False),
            sqlalchemy.Column("photo_url", sqlalchemy.String(255)),
            sqlalchemy.Column("created_at", sqlalchemy.DateTime, nullable=False,
                                server_default=sqlalchemy.func.now()),
            sqlalchemy.Column(
                "last_modified_at",
                sqlalchemy.DateTime,
                nullable=False,
                server_default=sqlalchemy.func.now(),
                onupdate=sqlalchemy.func.now(),
                ),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


################################ FastAPI App ################################
app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CustomHTTPBearer(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)
        
        try:
            payload = jwt.decode(res.credentials, config('JWT_SECRET'), algorithms=['HS256'])
            user = await database.fetch_one(users.select().where(users.c.id == payload["sub"]))
            request.state.user = user
            return payload
        except jwt.ExpiredSignatureError:
            raise jwt.HTTPException(401, "Token expired.")
        except jwt.InvalidTokenError:
            raise jwt.HTTPException(401, "Invalid token.")


oauth2_scheme = CustomHTTPBearer()


def create_access_token(user):
    try:
        payload = {
            "sub": user["id"], 
            "exp": datetime.utcnow() + timedelta(minutes=120)
        }
        return jwt.encode(payload, config("JWT_SECRET"), algorithm="HS256")
    except Exception as e:
        raise e

async def is_admin(request: Request):
    user = request.state.user
    if not user or user["role"] not in (UserRolesEnum.admin, UserRolesEnum.super_admin):
        raise jwt.HTTPException(403, "You do not have permissions for this resource")

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class EmailField(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v) -> str:
        try:
            validate_e(v)
            return v
        except EmailNotValidError:
            raise ValueError("Email is not valid!")


class BaseUser(BaseModel):
    email: EmailField
    full_name: str

    @validator("full_name")
    def validate_full_name(cls, v):
        try:
            first_name, last_name = v.split()
            return v
        except Exception:
            raise ValueError("You should provide the full name!")


class UserSignIn(BaseUser): # Request
    password: str


class UserSignOut(BaseUser): # Response
    phone: Optional[str]
    created_at: datetime
    last_modified_at: datetime

@app.post("/register", status_code=201)
async def create_user(user: UserSignIn):
    user.password = pwd_context.hash(user.password)
    q = users.insert().values(**user.dict())
    id_ = await database.execute(q)
    user_do = await database.fetch_one(users.select().where(users.c.id == id_))
    token = create_access_token(user_do)
    return {"token": token}


@app.get("/clothes", dependencies=[Depends(oauth2_scheme)]) # Only logged users can have access
async def get_all_clothes():
    return await database.fetch_all(clothes.select())

class ClothesBase(BaseModel):
    name: str
    photo_url: str
    size: SizeEnum
    color: ColorEnum


class ClothesIn(ClothesBase):
    pass 


class ClothesOut(ClothesBase):
    id: int
    created_at: datetime
    last_modified_at: datetime


@app.post("/clothes/", response_model=ClothesOut, status_code=201,
                        dependencies=[Depends(oauth2_scheme), Depends(is_admin)])
async def create_clothes(clothes_data: ClothesIn):
    id_ = await database.execute(clothes.insert().values(**clothes_data.dict()))
    return await database.fetch_one(clothes.select().where(users.c.id == id_))

