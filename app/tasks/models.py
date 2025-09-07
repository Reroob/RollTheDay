from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class TaskCategory(SQLModel,table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="useraccount.id")
    taskname: str
    weight: int
    priority: bool
    dailylimit: int
    totallimit: int
    enabled: bool
    colour: str  # Hex format: #RRGGBB (e.g., #FF5733)


class SubTasks(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    task_category_id: int = Field(foreign_key="taskcategory.id")
    taskname: str
    weight: int
    priority: bool
    dailylimit: int
    totallimit: int
    enabled: bool
       