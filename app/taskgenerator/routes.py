import logging
from typing import List
from app.taskgenerator.models import SelectableTask
from fastapi import APIRouter, Depends, HTTPException
from app.taskgenerator.schemas import GeneratorInputRead, GeneratorOutputRead, TaskChosenListRead, TaskChosenRead, RandomTaskTitleRead
from app.taskgenerator.generator import  task_selector, task_list_selector, task_list_selector_by_userid, format_task_list
from app.core.db import get_session
from sqlmodel import Session
import random
logger = logging.getLogger(__name__)

router = APIRouter(prefix='/taskgenerator', tags=['taskgenerator'])

@router.post('/randomise_task_list', response_model=List[TaskChosenRead])
async def randomise_task_list(generator_input: GeneratorInputRead, session: Session = Depends(get_session)):  
    tasklist = generator_input.selectabletasklist
    randomised_task_list = task_list_selector(tasklist)
    logger.info(f"Randomised task list: {randomised_task_list}")
    return randomised_task_list

@router.post('/random_task', response_model=TaskChosenRead)
async def random_task(tasklist: List[SelectableTask], session: Session = Depends(get_session)):
    randomised_task = task_selector(tasklist)
    return randomised_task

@router.post('/random_task_list_Setcount', response_model=List[RandomTaskTitleRead])
async def random_task_list_Setcount(userid: int = 1, session: Session = Depends(get_session), taskcount: int = 1):
    random_list = []
    user_task_list = task_list_selector_by_userid(userid)
    tasklist = task_list_selector_by_userid(userid)
    for i in range(taskcount):
        random_task = task_selector(tasklist)
        if not random_task.parentcategoryname:
            random_list.append(RandomTaskTitleRead(task=random_task.tasktitle))
        else:
            random_list.append(RandomTaskTitleRead(task=f'{random_task.parentcategoryname}: {random_task.tasktitle}'))   
    return random_list

@router.post('/random_task_list_by_userid_count', response_model=List[RandomTaskTitleRead])
async def random_task_list_by_userid_count(userid: int = 1, session: Session = Depends(get_session), taskcount: int = 1):
    random_list = task_list_selector_by_userid(userid, taskcount)
    formatted_list = format_task_list(random_list)
    return formatted_list









