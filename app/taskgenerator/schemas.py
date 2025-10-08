from pydantic import BaseModel
from typing import List
from app.taskgenerator.models import SelectableTask
from typing import Optional


class ScheduleSettingsRead(BaseModel):
    slotcount: int
    daycount: int
    dailyslotcount: int

class ScheduleSettingsCreate(BaseModel):
    slotcount: int
    daycount: int
    dailyslotcount: int

class ScheduleSettingsUpdate(BaseModel):   
    slotcount: Optional[int] = None
    daycount: Optional[int] = None
    dailyslotcount: Optional[int] = None


class GeneratorInputRead(BaseModel):
    schedule_settings: ScheduleSettingsRead
    selectabletasklist: List[SelectableTask]
    model_config = {"from_attributes": True}

class TaskChosenRead(BaseModel):
    tasktitle: str
    category_colour: str
    parentcategoryname: str | None = None
    model_config = {"from_attributes": True}

class TaskChosenListRead(BaseModel):
    taskchosenlist: List[TaskChosenRead]
    model_config = {"from_attributes": True}

class GeneratorOutputRead(BaseModel):
    randomtasklist: List[TaskChosenRead]
    model_config = {"from_attributes": True}

class RandomTaskTitleRead(BaseModel):
    task: str


class TaskPercentageRead(BaseModel):
    taskpercentages: dict[str, int]


