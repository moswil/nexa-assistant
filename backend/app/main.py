"""
Main application entrypoint.

Initializes the FastAPI app and routes.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.v1.routes import get_routes
from app.container import question_service

app = FastAPI(
    title="Minimal Assistant API",
    version="1.0.0",
    description="A clean-architecture-based backend assistant"
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Mount v1 routes
app.include_router(get_routes(question_service), prefix="/api/v1")
