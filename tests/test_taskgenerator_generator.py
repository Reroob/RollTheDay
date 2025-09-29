import pytest

from app.taskgenerator.generator import task_selector
from app.taskgenerator.schemas import TaskChosenRead, GeneratorInputRead, GeneratorOutputRead, ScheduleSettingsRead, TaskChosenListRead
from app.taskgenerator.models import SelectableTask
from app.tasks.schemas import TaskCategoryRead, SubTasksRead, CategorySubtaskListRead, UserTaskListFullRead
from uuid import uuid4

TEST_UUID1 = uuid4()
TEST_UUID2 = uuid4()
TEST_UUID3 = uuid4()
TEST_UUID4 = uuid4()
TEST_UUID5 = uuid4()
TEST_UUID6 = uuid4()
TEST_UUID7 = uuid4()
TEST_UUID8 = uuid4()
TEST_UUID9 = uuid4()
TEST_UUID10 = uuid4()

FULLTASKLIST_NOSUBTASKS: CategorySubtaskListRead = (
    CategorySubtaskListRead(      taskcategory= TaskCategoryRead(
        title="Housework",
        weight=20,
        priority=False,
        dailylimit=1000,
        totallimit=1000,
        enabled=True,
        colour="#808080",
        tasktype=1,
        public_id=TEST_UUID1
      ),
      subtasks=[]
    ),
    CategorySubtaskListRead(
      taskcategory= TaskCategoryRead(
        title="Coding",
        weight=10,
        priority=False,
        dailylimit=1000,
        totallimit=1000,
        enabled=True,
        colour="#808080",   
        tasktype=1,
        public_id=TEST_UUID2
      ),
      subtasks=[]
    ),
    CategorySubtaskListRead(
      taskcategory= TaskCategoryRead(
        title="Blender",
        weight=40,
        priority=False,
        dailylimit=1000,
        totallimit=1000,
        enabled=True,
        colour="#808080",
        tasktype=1,
        public_id=TEST_UUID3
      ),
      subtasks=[]
    ),
  )
