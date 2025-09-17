import logging

from app.tasks.schemas import CategorySubtaskListRead, UserTaskListFullRead , TaskCategoryRead, SubTasksRead
from app.taskgenerator.models import SelectableTask

from typing import List




def convert_category_to_selectabletask(category: TaskCategoryRead) -> SelectableTask:
    returned_category = SelectableTask(
        public_id=category.public_id,
        tasktype=category.tasktype,
        title=category.title,
        parentcategoryname=None,
        dailylimit=category.dailylimit,
        totallimit=category.totallimit,
        ratioweight=category.weight,
        prioritypending=category.priority,
        category_colour=category.colour
    )
    return SelectableTask.model_validate(returned_category)

def convert_subtask_to_selectabletask(subtask) -> SelectableTask:
    returned_subtask = SelectableTask(
        public_id=subtask.public_id,
        tasktype=subtask.tasktype,
        title=subtask.title,
        dailylimit=subtask.dailylimit,
        totallimit=subtask.totallimit,
        prioritypending=subtask.priority,
        ratioweight=subtask.weight
    )
    return SelectableTask.model_validate(returned_subtask)

def calculate_subtask_weight(subtask_weight, total_subtask_weight, category_weight) -> float:   
    ratio_weight = subtask_weight / total_subtask_weight
    calculated_weight = category_weight * ratio_weight  
    return round(calculated_weight, 2)

def calculate_user_task_list(user_task_list: UserTaskListFullRead) -> list[SelectableTask]:
    task_list = []
    for category_subtask_list in user_task_list.tasklist:
        task_list.extend(calculate_category_tasks(category_subtask_list))
    return task_list
    
def calculate_category_tasks(category_subtask_list: CategorySubtaskListRead) -> list[SelectableTask]:
    print(f"Calculating category tasks for {category_subtask_list}")
    task_list = []
    category = category_subtask_list.taskcategory
    subtasks = category_subtask_list.subtasks
    total_subtask_weight = 0
    if len(subtasks) == 0:
        converted_category = convert_category_to_selectabletask(category)
        task_list.append(converted_category)
        return task_list
    for subtask in subtasks:
        total_subtask_weight += subtask.weight
    for subtask in subtasks:
        converted_subtask = convert_subtask_to_selectabletask(subtask)
        converted_subtask.ratioweight = calculate_subtask_weight(subtask.weight, total_subtask_weight, category.weight)
        converted_subtask.parentcategoryname = category.title
        converted_subtask.category_colour = category.colour
        task_list.append(converted_subtask)
    return task_list



    

  
