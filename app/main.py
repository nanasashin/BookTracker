from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend's URL
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the expected data structure for POST requests
class ButtonPayload(BaseModel):
  	message: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/api")
async def handle_button_click(payload: ButtonPayload):
  print(f"Received from frontend: {payload.message}")
  return {"status": "success", "reply": f"Server received: {payload.message}"}