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


def update_category(session: Session, category_public_id: UUID, category_update: schemas.TaskCategoryUpdate) -> Optional[models.TaskCategory]:
    """Update an existing task category
    
    Args:
        session: The database session
        category_public_id: The public ID of the category to update (no pk)
        category_update: The update data for the category

    Returns:
        The updated category
    """

    db_category = get_category_by_uuid(session, category_public_id)
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



def delete_category_by_uuid(session: Session, category_id: UUID) -> Optional[models.TaskCategory]:
    """Delete a task category by UUID"""
    statement = select(models.TaskCategory).where(models.TaskCategory.public_id == category_id)
    db_category = session.exec(statement).first()
    if not db_category:
        return None
    session.delete(db_category)
    session.commit()
    return db_category



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
    statement = select(models.SubTasks).where(models.SubTasks.public_id == subtask_id)
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
    statement = select(models.SubTasks).where(models.SubTasks.public_id == subtask_id)
    return session.exec(statement).first()
    

def get_subtask_by_uuid(session: Session, subtask_public_id: UUID) -> Optional[models.SubTasks]:
    """Get a subtask by UUID"""
    statement = select(models.SubTasks).where(models.SubTasks.public_id == subtask_public_id)
    return session.exec(statement).first()
    

def delete_subtask_by_uuid(session: Session, subtask_id: UUID) -> Optional[models.SubTasks]:
    """Delete a subtask by ID"""

    statement = select(models.SubTasks).where(models.SubTasks.public_id == subtask_id)       
    db_subtask = session.exec(statement).first()
    if not db_subtask:
        return None
    session.delete(db_subtask)
    session.commit()
    return db_subtask

   


def get_subtasks_by_categoryid(session: Session, taskcategory_id: int) -> List[models.SubTasks]:
    """Get all subtasks by category ID"""
    statement = select(models.SubTasks).where(models.SubTasks.taskcategory_id == taskcategory_id)
    logger.info(f'Getting subtasks by category id: {taskcategory_id}')
    return session.exec(statement).all()


def get_subtasks_by_category_publicid(session: Session, taskcategory_public_id: UUID) -> List[models.SubTasks]:
    """Extract all subtasks with matching task_category_uuid (all child subtasks)"""
    logger.info(f'Getting subtasks by category id: {taskcategory_public_id}')
    try: 
        category = get_category_by_uuid(session, taskcategory_public_id)
        statement = select(models.SubTasks).where(models.SubTasks.taskcategory_id == category.id)
        return session.exec(statement).all()
    except Exception as e:
        logger.error(f'Error getting subtasks by category public id: {e}')
        return None    


"""
def get_user_by_userid(session: Session, userid: int) -> Optional[models.UserAccount]:
    Get a user by userid
    statement = select(models.UserAccount).where(models.UserAccount.id == userid)
    return session.exec(statement).first()
"""

def get_categories_by_userid(session: Session, user_public_id: UUID) -> List[models.TaskCategory]:
    """Extract list of all categories for a specified user_id"""
    statement = select(models.TaskCategory).where(models.TaskCategory.useraccount_id == user_public_id)
    return session.exec(statement).all()





