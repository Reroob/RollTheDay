from fastapi import FastAPI, HTTPException,Depends, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.core.logs import logger
from app.core.db import create_tables, create_default_admin_user
from app.core.config import settings
from app.tasks.routes import router as tasks_router
from app.taskgenerator.routes import router as taskgenerator_router

logger=logging.getLogger(__name__)


logger.info(f"Starting in Environment: {settings.environment}")
logger.info(f"env var check: {settings.envvar}")

if settings.environment == "development":
    logger.info(f"Creating tables in development environment")
    create_tables()
    create_default_admin_user()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(tasks_router)
app.include_router(taskgenerator_router)

# Serve the main page at root
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

