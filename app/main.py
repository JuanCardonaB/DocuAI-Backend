from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload_file
from app.routes import ask

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_file.router)
app.include_router(ask.router)