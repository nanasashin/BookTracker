from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import tomllib
import os
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()
base_dir = Path(os.environ.get("WORKING_DIR"))

with open(os.environ.get("BOOK_TRACKER_CONFIG", "../conf.toml"), "rb") as f:
    cfg = tomllib.load(f)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return FileResponse(base_dir / cfg["html"]["book"])

@app.get("/api/test")
def test():
	return cfg

html_dir = base_dir / "web" / "book" 
app.mount("/", StaticFiles(directory=html_dir, html=True), name="static")
