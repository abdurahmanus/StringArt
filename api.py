from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn
from pydantic import BaseModel

class GenerateParams(BaseModel):
    name: str | None = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from Fastapi"} 

@app.post("/generate")
async def generate(params: GenerateParams):
    return params

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)