import logging
from uuid import UUID
from sqlmodel import Session, select
from typing import List, Optional
from . import models, schemas

logger = logging.getLogger(__name__)

# Util functions #########################################################

def map_subtask_to_dbmodel(session: Session, subtask: schemas.SubTasksCreate) -> models.SubTasks:
    """Map API create subtask to DB schema"""
    category = get_category_by_uuid(session, subtask.taskcategory_public_id)
    model_data = subtask.model_dump()
    model_data['taskcategory_id'] = category.id
    logger.info(f'Mapped subtask to db: {model_data}')
    logger.info(f'Mapped subtask to dbmodel: {models.SubTasks(**model_data)}')
    return models.SubTasks(**model_data)


# CRUD functions #########################################################


def create_category(session: Session, category: schemas.TaskCategoryCreate, userid: int) -> models.TaskCategory:
    """Create a new task category in the database"""
    try:
        db_category = models.TaskCategory(**category.model_dump(), useraccount_id=userid)
        session.add(db_category)
        session.commit()
        session.refresh(db_category)
        return db_category
    except Exception as e:
        logger.debug(f'CRUD Error - create_category: {e}')
        return None


def update_category(session: Session, category_id: UUID, category_update: schemas.TaskCategoryUpdate) -> Optional[models.TaskCategory]:
    """Update an existing task category"""

    db_category = session.get(models.TaskCategory, category_id)
    if not db_category:
        return None    
    update_data = category_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_category, field, value)
    
        session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category



def get_category_by_id(session: Session, category_id: UUID) -> Optional[models.TaskCategory]:
    """Get a task category by ID"""
    statement = select(models.TaskCategory).where(models.TaskCategory.idexternal == category_id)
    return session.exec(statement).first()

def get_category_by_uuid(session: Session, category_uuid: UUID) -> Optional[models.TaskCategory]:
    """Get a task category by UUID"""
    statement = select(models.TaskCategory).where(models.TaskCategory.public_id == category_uuid)
    return session.exec(statement).first()


def delete_category_by_id(session: Session, category_id: UUID) -> bool:
    """Delete a task category by ID"""
    statement = select(models.TaskCategory).where(models.TaskCategory.idexternal == category_id)
    db_category = session.exec(statement).first()
    if not db_category:
        return False
    
    session.delete(db_category)
    session.commit()
    return True


def create_subtask(session: Session, subtask: schemas.SubTasksCreate, userid: int) -> models.SubTasks:
    """Create a new subtask in the database"""
    db_subtask = map_subtask_to_dbmodel(session, subtask)
    logger.info(f'Create subtask create_subtask: {db_subtask}')
    session.add(db_subtask)
    session.commit()
    session.refresh(db_subtask)
    return subtask


def update_subtask(session: Session, subtask_id: UUID, subtask_update: schemas.SubTasksUpdate) -> Optional[models.SubTasks]:
    """Update an existing subtask"""
    statement = select(models.SubTasks).where(models.SubTasks.idexternal == subtask_id)
    db_subtask = session.exec(statement).first()
    if not db_subtask:
        return None
    
    update_data = subtask_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_subtask, field, value)
    
    session.add(db_subtask)
    session.commit()
    session.refresh(db_subtask)
    return db_subtask


def get_subtask_by_id(session: Session, subtask_id: UUID) -> Optional[models.SubTasks]:
    """Get a subtask by ID"""
    statement = select(models.SubTasks).where(models.SubTasks.id == subtask_id)
    return session.exec(statement).first()
    
def get_subtasks_by_categoryid(session: Session, taskcategory_id: int) -> List[models.SubTasks]:
    """Get all subtasks by category ID"""
    statement = select(models.SubTasks).where(models.SubTasks.taskcategory_id == taskcategory_id)
    return session.exec(statement).all()

def get_subtask_by_uuid(session: Session, subtask_public_id: UUID) -> Optional[models.SubTasks]:
    """Get a subtask by UUID"""
    statement = select(models.SubTasks).where(models.SubTasks.public_id == subtask_public_id)
    return session.exec(statement).first()
    

def delete_subtask_by_id(session: Session, subtask_id: UUID) -> bool:
    """Delete a subtask by ID"""
    statement = select(models.SubTasks).where(models.SubTasks.id == subtask_id)
    db_subtask = session.exec(statement).first()
    if not db_subtask:
        return False    
    session.delete(db_subtask)
    session.commit()
    return True


def get_subtasks_by_catid(session: Session, task_category_public_id: UUID) -> List[models.SubTasks]:
    """Extract all subtasks with matching task_category_public_id (all child subtasks)"""
    logger.info(f'Getting subtasks by category id: {task_category_public_id}')
    try: 
        category = get_category_by_uuid(session, task_category_public_id)
        query = select(models.SubTasks).where(models.SubTasks.TaskCategory_id == category.id)
        return session.exec(query).all()
    except Exception as e:
        logger.error(f'Error getting subtasks by category public id: {e}')
        return None    



def get_categories_by_userid(session: Session, user_public_id: UUID) -> List[models.TaskCategory]:
    """Extract list of all categories for a specified user_id"""
    statement = select(models.TaskCategory).where(models.TaskCategory.useraccount_id == user_public_id)
    return session.exec(statement).all()




