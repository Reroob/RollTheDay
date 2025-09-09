import logging
from sqlmodel import Session
from fastapi import APIRouter, HTTPException, Depends
from app.core.db import get_session
from app.tasks import logic
from app.tasks import crud
from app.tasks import schemas
from uuid import UUID

logger = logging.getLogger(__name__)

router = APIRouter(prefix='/tasks', tags=['tasks'])

## Get Endpoints #########################################################

@router.get('/get_categories_by_userid', response_model=list[schemas.TaskCategoryRead])
async def get_categories_by_user_id(session: Session = Depends(get_session), userid: int = 1):
    try:
        return crud.get_categories_by_userid(session, userid)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Database Error: get categories by userid: {e}')
        raise HTTPException(status_code=500, detail="Could not get Categories information")

@router.get('/get_category_by_id', response_model=schemas.TaskCategoryRead)
async def get_category_by_id(session: Session = Depends(get_session), categoryid: UUID = 1):
    try:
        category = crud.get_category_by_uuid(session, categoryid)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Database Error: get category by id: {e}')
        raise HTTPException(status_code=500, detail="Could not get Category information")

@router.get('/get_subtask_by_id', response_model=schemas.SubTasksRead)
async def get_subtask_by_id(session: Session = Depends(get_session), subtaskid: UUID = 1):
    try:
        result = crud.get_subtask_by_uuid(session, subtaskid)
        if not result:
            raise HTTPException(status_code=404, detail="Subtask not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Database Error: get subtask by id: {e}')
        raise HTTPException(status_code=500, detail=f"Could not get Subtask information")

@router.get('/get_subtasks_by_categoryid', response_model=schemas.CategorySubtaskListRead)
async def get_subtasks_by_categoryid (categoryid: UUID, session: Session = Depends(get_session)):
    try:
        taskcategory= crud.get_category_by_uuid(session, categoryid) #return models.TaskCategory
        subtasks_extracted = crud.get_subtasks_by_categoryid(session, taskcategory.id)
        subtasks = []
        for subtask in subtasks_extracted:
            logger.info(f'Subtask: {subtask}')
            subtasks.append(schemas.SubTasksRead.model_validate(subtask))

        logger.info(f'\n\nSubtasks: {subtasks}\n') #return models.SubTasks
        if not taskcategory:
            raise HTTPException(status_code=404, detail="Category not found")  
        return schemas.CategorySubtaskListRead(taskcategory=taskcategory, subtasks=subtasks ) 
        raise
    except Exception as e:
        logger.error(f'route error: unable to get subtasks by cat id: {e}')
        raise HTTPException(status_code=500, detail="Could not get subtask information ")

     

@router.get('/get_user_full_tasks', response_model=schemas.UserTaskListFullRead)
def get_user_full_tasks(session: Session = Depends(get_session), userid: int  = 1):
        try:
            completetasklist = []
            categorylist= crud.get_categories_by_userid(session, userid)
            logger.info(f'Category list: {categorylist}')
            for category in categorylist:
                subtasks = crud.get_subtask_by_id(session, category.id)
                completetasklist.append({"taskcategory": category, "subtasks": subtasks })
            if not categorylist:
                raise HTTPException(status_code=404, detail="Category list not found")
            return {"tasklist":completetasklist}
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f'unable to generate user full tasks: {e}')
            raise HTTPException(status=500, detail="unable to get user task list")


## Post Endpoints #########################################################

@router.post('/create_category', response_model=schemas.TaskCategoryCreate)
async def create_category(category_in: schemas.TaskCategoryCreate, session: Session = Depends(get_session),  userid: int = 1):
    try:
        result = crud.create_category(session, category_in, userid)
        if not result:
            raise HTTPException(status_code=404, detail="Category not created")
        return result
    except HTTPException:
        raise
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Database error: create category : {e}')
        raise HTTPException(status_code=500, detail=f"could not create category")   


@router.post('/create_subtask', response_model=schemas.SubTasksCreate)
async def create_subtask( subtask_in: schemas.SubTasksCreate, session: Session = Depends(get_session), userid: int = 1 ):
    try:
        logger.info(f'Creating subtask: {subtask_in}')
        result = crud.create_subtask(session, subtask_in, userid)
        if not result:
            raise HTTPException(status_code=404, detail="Subtask not created")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Database error: create subtask : {e}')
        raise HTTPException(status_code=500, detail=f"could not create subtask")   

## Patch Endpoints #########################################################

@router.patch('/update_category_by_uuid', response_model=schemas.TaskCategoryUpdate)
async def update_category_by_uuid(category_in: schemas.TaskCategoryUpdate, session: Session = Depends(get_session), userid: int = 1):
    try:
        result = crud.update_category(session, category_in)
        if not result:
            raise HTTPException(status_code=404, detail="Category not updated")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Unable to update category')
        raise HTTPException(status_code=500, detail='Could not update category')

@router.patch('/update_subtask_by_uuid', response_model=schemas.SubTasksUpdate)
async def update_subtask_by_uuid(subtask_in: schemas.SubTasksUpdate, session: Session = Depends(get_session), userid: int = 1):
    try:
        result = crud.update_subtask(session, subtask_in)
        if not result:
            raise HTTPException(status_code=404, detail="Subtask not updated")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Unable to update subtask')
        raise HTTPException(status_code=500, detail='Could not update subtask')

@router.delete('/delete_category_by_uuid', response_model=schemas.TaskCategoryUpdate)
async def delete_category(categoryid: UUID, session: Session = Depends(get_session), userid: int = 1):
    try:
        result = crud.delete_category_by_id(session, categoryid)
        if not result:
            raise HTTPException(status_code=404, detail="Category not deleted")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Unable to delete category')
        raise HTTPException(status_code=500, detail='Could not delete category')

## Delete Endpoints #########################################################

@router.delete('/delete_subtask_by_uuid', response_model=schemas.SubTasksUpdate)
async def delete_subtask(subtaskid: UUID, session: Session = Depends(get_session), userid: int = 1):
    try:
        result = crud.delete_subtask_by_uuid(session, subtaskid)
        if not result:
            raise HTTPException(status_code=404, detail="Subtask not deleted")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Unable to delete subtask')
        raise HTTPException(status_code=500, detail='Could not delete subtask')
    
@router.delete('/delete_category', response_model=schemas.TaskCategoryUpdate)
async def delete_category(categoryid: UUID, session: Session = Depends(get_session), userid: int = 1):
    try:
        result = crud.delete_category_by_id(session, categoryid)
        if not result:
            raise HTTPException(status_code=404, detail="Category not deleted")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f'Unable to delete category')
        raise HTTPException(status_code=500, detail='Could not delete category')


