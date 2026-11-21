import uvicorn

from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend's URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_index():
    return FileResponse("../web/book/index.html")

@app.get("/api/test")
def test():
	return {"message": "test"}

html_dir = Path(__file__).resolve().parent.parent / "web"

app.mount("/", StaticFiles(directory=html_dir, html=True), name="static")
