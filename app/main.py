from pathlib import Path
import tomllib

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import Field, SQLModel

from pydantic import BaseModel

from database import create_db_and_tables, get_engine

class Book(BaseModel):
    title: str
    author: str
    genre: str

class BookDB(Book):
    id: int | None = Field(default=None, primary_key=True)



@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    SQLModel.metadata.create_all(get_engine())

    yield

app = FastAPI(lifespan=lifespan)
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
    book_dict = book.model_dump()
    return {"book_dict": book_dict, "status": "valid"}

@app.get("/app/jquery")
async def jquery():
    return FileResponse(BASE_DIR / cfg["import"]["jquery"])

app.mount("/", StaticFiles(directory=BASE_DIR / "web" / "book" , html=True), name="static")

