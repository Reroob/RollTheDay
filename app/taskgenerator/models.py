from functools import total_ordering
from queue import PriorityQueue
from pydantic import BaseModel
from typing import List
from uuid import UUID


class SelectableTask(BaseModel):
    public_uuid: UUID
    task_type: int
    tasktitle: str
    parentcategoryname: str = None
    dailylimit: int = 1000
    totallimit: int = 1000
    ratioweight: float
    prioritypending: bool

class TaskChosen(BaseModel):
    tasktitle: str
    category_name: str

class TaskGeneratorInput(BaseModel):
    selectabletasklist: List[SelectableTask]
    slotcount: int
    daycount: int
    dailyslotcount: int

class GeneratedRandomTaskList(BaseModel):
    randomtasklist: List[TaskChosen]



