from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import Field, Session, SQLModel, create_engine, select

from pydantic import BaseModel

import tomllib

class Book(BaseModel):
    title: str
    author: str
    genre: str

class BookDB(Book):
    id: int | None = Field(default=None, primary_key=True)

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "conf.toml", "rb") as f:
    cfg = tomllib.load(f)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return FileResponse(BASE_DIR / cfg["html"]["book"])

@app.get("/api/test")
def test():
    return {"ok": "ok"}

@app.post("/api/book/")
def create_book(book: Book):
    book_db: BookDB = book.model_validate(BookDB)
    book_db.id = 10
    book_dict = book_db.model_dump()
    return book_dict


@app.get("/app/jquery")
async def jquery():
    return FileResponse(BASE_DIR / cfg["import"]["jquery"])

app.mount("/", StaticFiles(directory=BASE_DIR / "web" / "book" , html=True), name="static")

