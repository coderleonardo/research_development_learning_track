import databases
import sqlalchemy

import urllib.parse
from decouple import config

from fastapi import FastAPI, Request

URL_PARSE = urllib.parse.quote_plus(config('DB_PASSWORD'))
DATABASE_URL = f"postgresql://{config('DB_USER')}:{URL_PARSE}@localhost:{config('DB_PORT')}/{config('DATABASE')}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Tables of the database
books = sqlalchemy.Table(
    "books", 
    metadata, 
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), 
    sqlalchemy.Column("title", sqlalchemy.String), 
    sqlalchemy.Column("author", sqlalchemy.String), 
    sqlalchemy.Column("pages", sqlalchemy.Integer), 
)

readers = sqlalchemy.Table(
    "readers", 
    metadata, 
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), 
    sqlalchemy.Column("first_name", sqlalchemy.String), 
    sqlalchemy.Column("last_name", sqlalchemy.String), 
)


readers_books = sqlalchemy.Table(
    "readers_books", 
    metadata, 
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), 
    sqlalchemy.Column("book_id", sqlalchemy.ForeignKey("books.id"), nullable=False), 
    sqlalchemy.Column("reader_id", sqlalchemy.ForeignKey("readers.id"), nullable=False),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


################################ FastAPI App ################################
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/books")
async def get_all_books():
    query = books.select()
    return await database.fetch_all(query)


@app.post("/books")
async def create_book(request: Request):
    data = await request.json()
    query = books.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


@app.post("/readers")
async def create_book(request: Request):
    data = await request.json()
    query = readers.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}

@app.post("/read")
async def read_book(request: Request):
    data = await request.json()
    query = readers_books.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}
