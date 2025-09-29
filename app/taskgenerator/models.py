from functools import total_ordering
from queue import PriorityQueue
from pydantic import BaseModel
from typing import List
from uuid import UUID


class SelectableTask(BaseModel):
    public_id: UUID
    tasktype: int
    title: str
    parentcategoryname: str | None = None
    dailylimit: int
    totallimit: int
    ratioweight: float
    prioritypending: bool
    category_colour: str = "#808080"












