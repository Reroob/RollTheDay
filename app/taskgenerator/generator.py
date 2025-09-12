from random import randint, choice, choices
from app.taskgenerator.models import SelectableTask
from app.tasks.schemas import TaskCategoryRead, UserTaskListFullRead, TaskCategoryRead, SubTasksRead
from typing import List, Optional




def task_selector(tasklist: UserTaskListFullRead, slotcount: int):
    category_list = 
    # select random category from tasklist based on weight
    # if category has subtasks, select random subtask from subtasks based on weight
    # return task category if no subtasks, otherwisereturn subtask
   pass


def generate_task_list(tasklist: UserTaskListFullRead) -> List[SelectableTask]:

    pass


def calculate_subtask_weight(subtasklist: List[SubTasksRead]) -> float:
    pass


