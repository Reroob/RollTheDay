from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


# TaskCategory Schemas
class TaskCategoryBase(BaseModel):
    taskname: str
    weight: int = 25
    priority: bool = False
    dailylimit: int = 0
    totallimit: int = 0
    enabled: bool = True
    colour: str  = "#808080"

class TaskCategoryCreate(TaskCategoryBase):
    pass

    # All fields from base have defaults except taskname, colour, and user_id

class TaskCategoryRead(TaskCategoryBase):
    public_id: UUID

class TaskCategoryUpdate(BaseModel):
    taskname: Optional[str] = None
    weight: Optional[int] = None
    priority: Optional[bool] = None
    dailylimit: Optional[int] = None
    totallimit: Optional[int] = None
    enabled: Optional[bool] = None
    colour: Optional[str] = None

class TaskCategoryInDB(TaskCategoryBase):
    id: int
    user_id: int    
    public_id: UUID


# SubTasks Schemas
class SubTasksBase(BaseModel):
    taskname: str
    weight: int = 25
    priority: bool = False
    dailylimit: int = 0
    totallimit: int = 0
    enabled: bool = True

class SubTasksCreate(SubTasksBase):
    taskcategory_public_id: UUID

class SubTaskCreateDB(SubTasksBase):
    taskcategory_id: int
       # All fields from base have defaults except taskname and task_category_id

class SubTasksRead(SubTasksBase):
    public_id: UUID

class SubTasksUpdate(BaseModel):
    taskname: Optional[str] = None
    weight: Optional[int] = None
    priority: Optional[bool] = None
    dailylimit: Optional[int] = None
    totallimit: Optional[int] = None
    enabled: Optional[bool] = None

class SubTasksInDB(SubTasksBase):
    id: int
    taskcategory_id: int
    public_id: UUID

class CategorySubtaskListRead(BaseModel):
    taskcategory: TaskCategoryRead
    subtasks: List[SubTasksRead]

class UserTaskListFullRead(BaseModel):
    tasklist: List[CategorySubtaskListRead]