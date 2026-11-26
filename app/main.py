from pathlib import Path
import tomllib

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import SQLModel

from database import create_db_and_tables, get_engine
from table import * 

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

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


@app.get("/external/jquery")
async def jquery():
    return FileResponse(BASE_DIR / cfg["import"]["jquery"])

app.mount("/", StaticFiles(directory=BASE_DIR / "web" / "book" , html=True), name="static")

