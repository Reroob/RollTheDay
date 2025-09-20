from sqlmodel import create_engine, Session, SQLModel, select
from datetime import date
import logging
from app.core.config import settings
from app.tasks import models as tasks_models  # noqa: F401  Ensure models imported for metadata
from app.user_account import models as user_models  # noqa: F401


logger= logging.getLogger(__name__)

engine = None
try:
    engine = create_engine(settings.database_url)
    logger.info("Database engine created successfully")
except Exception as e:
    logger.error(f'Unable to create engine: {e}')

def get_session():
    if engine is None:
        raise RuntimeError("Database engine is not initialized")
    try:
        session = Session(engine)
        yield session
    except Exception as e:
        logger.error(f'Error in get_session: {e}. rolling back and closing session')
        session.rollback()
        session.close()
    finally:
        session.rollback()
        session.close()

def create_tables():
    if engine is None:
        logger.error("Database table creation failed: Engine is not initialized")
        return
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f'Database table creation failed: {e}')


def create_default_admin_user():
    """Check for default admin user (userid=1) and create if it doesn't exist"""
    if engine is None:
        logger.error("Failed to create default admin user: Engine is not initialized")
        return
    try:
        with Session(engine) as session:
            # Check if user with id=1 exists
            statement = select(user_models.UserAccount).where(user_models.UserAccount.id == 1)
            existing_user = session.exec(statement).first()
            
            if existing_user:
                logger.info("Default admin user already exists")
                return
            
            # Hash the default admin password
            hashed_password = settings.default_admin_password
            
            # Create default admin user
            default_user = user_models.UserAccount(
                id=1,
                email=settings.default_admin_email,
                hashedpassword=hashed_password,
                is_validated=True,
                is_admin=True,
                is_paid=True,
                subscriptionenddate=date(2099, 12, 31)  # Far future date   
            )
            
            session.add(default_user)
            session.commit()
            session.refresh(default_user)
            
            logger.info(f"Created default admin user: {settings.default_admin_email}")
            
    except Exception as e:
        logger.error(f'Failed to create default admin user: {e}')

