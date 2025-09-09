from fastapi import FastAPI, HTTPException,Depends, APIRouter
import logging
from app.core.logs import logger
from app.core.db import create_tables, create_default_admin_user
from app.core.config import settings
from app.tasks.routes import router as tasks_router

logger=logging.getLogger(__name__)

if settings.environment == "development":
    logger.info(f"Creating tables in development environment: testvar {settings.envvar}")
    create_tables()
    create_default_admin_user()

app = FastAPI()
app.include_router(tasks_router)

