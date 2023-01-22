import databases
import enum
import sqlalchemy

import urllib.parse
from decouple import config

from fastapi import FastAPI, Request
from pydantic import BaseModel, validator
from email_validator import validate_email as validate_e, EmailNotValidError
from typing import Optional
from datetime import datetime
from passlib.context import CryptContext

URL_PARSE = urllib.parse.quote_plus(config('DB_PASSWORD'))
DATABASE_URL = f"postgresql://{config('DB_USER')}:{URL_PARSE}@localhost:{config('DB_PORT')}/{config('DATABASE')}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

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
                onupdate=sqlalchemy.func.now(),
                ),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

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


################################ FastAPI App ################################
app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

@app.post("/register", status_code=201, response_model=UserSignOut)
async def create_user(user: UserSignIn):
    user.password = pwd_context.hash(user.password)
    q = users.insert().values(**user.dict())
    id_ = await database.execute(q)
    user = await database.fetch_one(users.select().where(users.c.id == id_))
    return user
