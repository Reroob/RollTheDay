import logging
from random import randint, choice, choices
from app.taskgenerator.models import SelectableTask
from app.taskgenerator.schemas import TaskChosenRead, GeneratorInputRead, GeneratorOutputRead, ScheduleSettingsRead, TaskChosenListRead, ScheduleSettingsCreate  
from app.tasks.schemas import TaskCategoryRead, UserTaskListFullRead, TaskCategoryRead, SubTasksRead
from typing import List, Optional
from app.taskgenerator.utils import calculate_user_task_list
import random
from app.tasks.utils import get_user_full_tasks
from app.taskgenerator.schemas import RandomTaskTitleRead

logger = logging.getLogger(__name__)





def get_selectabletasklist_by_userid(userid: int) -> list[SelectableTask]:
    tasklist = get_user_full_tasks(userid)
    return tasklist


def task_list_selector_by_userid(userid: int, listcount: int = 1) -> TaskChosenListRead:
    user_task_list = get_user_full_tasks(userid)
    logger.info(f"\n\n\n\n\n\************\nUser task list: {user_task_list}")
    tasklist = calculate_user_task_list(user_task_list)
    logger.info(f"Task list: {tasklist}")
    taskchosenlist = task_list_selector(tasklist, listcount)
    return taskchosenlist

def format_task_list(tasklist: List[TaskChosenRead]) -> List[RandomTaskTitleRead]:
    formatted_list = []
    for i in range(len(tasklist)):  
        if not tasklist[i].parentcategoryname:
            formatted_list.append(RandomTaskTitleRead(task=tasklist[i].tasktitle))
        else:
            formatted_list.append(RandomTaskTitleRead(task=f'{tasklist[i].parentcategoryname}: {tasklist[i].tasktitle}'))   
    return formatted_list


def task_list_selector(tasklist: list[SelectableTask], listcount: int = 1) -> TaskChosenListRead:
    randomisedtasklist = random.choices(tasklist, weights=[task.ratioweight for task in tasklist], k=listcount)    
    randomisedtasklist2 = random.choices(tasklist, weights=[task.ratioweight for task in tasklist], k=listcount)    
    combinedtasklist = randomisedtasklist + randomisedtasklist2
    random.shuffle(combinedtasklist)
    logger.info(f"\n\n\nlistcount: {listcount}\n***************\n")
    randomisedtasklist = randomisedtasklist[:listcount]
    taskchosenlist = []
    for task in randomisedtasklist:
        task = TaskChosenRead(tasktitle=task.title, category_name=task.parentcategoryname, category_colour=task.category_colour, parentcategoryname=task.parentcategoryname)
        taskchosenlist.append(task)
        logger.info(f"Task chosen: {task}")
    return taskchosenlist

def task_selector(tasklist: list[SelectableTask], listcount: int = 1) -> TaskChosenRead:
    logger.info(f"\n\n***************\nTask list for task selector: {tasklist}\n\n***************")
    randomisedtasklist = random.choices(tasklist, weights=[tasklist.ratioweight for tasklist in tasklist], k=listcount)
    taskchosenlist = []
    for task in randomisedtasklist:
        task = TaskChosenRead(tasktitle=task.title, category_name=task.parentcategoryname, category_colour=task.category_colour, parentcategoryname=task.parentcategoryname)
        taskchosenlist.append(task)
    return taskchosenlist[0]

def update_task_list(task: SelectableTask):
    if task.prioritypending:
        task.prioritypending = False
    task.totallimit -= 1
    return


def task_scheduler(tasklist: list[SelectableTask], schedule_settings: ScheduleSettingsRead) -> List[TaskChosenRead]:
    taskchosenlist = []
    prioritytasklist = []
    for task in tasklist:
        if task.totallimit == 0:
            tasklist.remove(task)
        elif task.prioritypending:
            prioritytasklist.append(task)
        else:
            continue

    


  





def calculate_subtask_weight(subtasklist: List[SubTasksRead]) -> float:
    pass


