from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, ForeignKey, Integer
from uuid import uuid4, UUID

class TaskCategory(SQLModel,table=True):
    id: int = Field(default=None, primary_key=True)
    public_id : UUID = Field(default_factory=lambda: str(uuid4()))
    useraccount_id: int = Field(
        sa_column=Column(
            Integer,
            ForeignKey("useraccount.id", ondelete="CASCADE"),
            nullable=False,
        )
    )
    title: str
    weight: int
    priority: bool
    dailylimit: int
    totallimit: int
    enabled: bool
    colour: str
    tasktype: int  # Hex format: #RRGGBB (e.g., #FF5733)
    
    # ORM relationship: deleting a category deletes its subtasks (delete-orphan)
    subtasks: List["SubTasks"] = Relationship(
        back_populates="category",
        sa_relationship_kwargs={"cascade": "all, delete-orphan", "passive_deletes": True},
    )


class SubTasks(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    public_id : UUID = Field(default_factory=lambda: str(uuid4()))
    taskcategory_id: int = Field(
        sa_column=Column(
            Integer,
            ForeignKey("taskcategory.id", ondelete="CASCADE"),
            nullable=False,
        )
    )
    title: str
    weight: int
    priority: bool
    dailylimit: int
    totallimit: int
    enabled: bool
    tasktype: int
    # ORM relationship back to parent category
    category: "TaskCategory" = Relationship(back_populates="subtasks")
       