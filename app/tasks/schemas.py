from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


# TaskCategory Schemas
class TaskCategoryBase(BaseModel):
    title: str
    weight: int = 25
    priority: bool = False
    dailylimit: int = 0
    totallimit: int = 0
    enabled: bool = True
    colour: str  = "#808080"
    tasktype: int = 1

class TaskCategoryCreate(TaskCategoryBase):
    pass


class TaskCategoryRead(TaskCategoryBase):
    public_id: UUID
    model_config = {"from_attributes": True} 

class TaskCategoryUpdate(BaseModel):
    title: Optional[str] = None
    weight: Optional[int] = None
    priority: Optional[bool] = None
    dailylimit: Optional[int] = None
    totallimit: Optional[int] = None
    enabled: Optional[bool] = None
    colour: Optional[str] = None

    model_config = {"from_attributes": True}

class TaskCategoryInDB(TaskCategoryBase):
    id: int
    user_id: int    
    public_id: UUID
    model_config = {"from_attributes": True}

class TaskCategoryDelete(BaseModel):
    public_id: UUID
    model_config = {"from_attributes": True}

class TaskCategoryCreateDB(TaskCategoryBase):
    user_id: int
    public_id: UUID
    model_config = {"from_attributes": True}


# SubTasks Schemas
class SubTasksBase(BaseModel):
    title: str
    weight: int = 25
    priority: bool = False
    dailylimit: int = 0
    totallimit: int = 0
    enabled: bool = True
    tasktype: int = 2
   

class SubTasksCreate(SubTasksBase):
    taskcategory_public_id: UUID
    




class SubTasksRead(SubTasksBase):
    public_id: UUID
    model_config = {"from_attributes": True}



class SubTasksUpdate(BaseModel):
    title: Optional[str] = None
    weight: Optional[int] = None
    priority: Optional[bool] = None
    dailylimit: Optional[int] = None
    totallimit: Optional[int] = None
    enabled: Optional[bool] = None
    model_config = {"from_attributes": True}

class SubTasksInDB(SubTasksBase):
    id: int
    taskcategory_id: int
    public_id: UUID    
    model_config = {"from_attributes": True}

class SubTasksDelete(BaseModel):
    public_id: UUID
    model_config = {"from_attributes": True}

class CategorySubtaskListRead(BaseModel):
    taskcategory: TaskCategoryRead
    subtasks: List[SubTasksRead]
    

class UserTaskListFullRead(BaseModel):
    tasklist: List[CategorySubtaskListRead]

class CategoryDelete(BaseModel):
    public_id: UUID
    title: str
    status: str = "deleted"
    model_config = {"from_attributes": True}
    
class SubtaskDelete(BaseModel):
    public_id: UUID
    title: str
    status: str = "deleted"
    model_config = {"from_attributes": True}

class CategorySubtaskDelete(BaseModel):
    category: CategoryDelete
    subtasks: List[SubtaskDelete]


