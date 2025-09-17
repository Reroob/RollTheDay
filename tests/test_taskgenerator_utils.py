import pytest

from uuid import uuid4

from app.taskgenerator.utils import     calculate_user_task_list, convert_category_to_selectabletask, convert_subtask_to_selectabletask,calculate_subtask_weight,calculate_category_tasks

from app.taskgenerator.models import SelectableTask
from app.tasks.schemas import TaskCategoryRead, SubTasksRead, CategorySubtaskListRead, UserTaskListFullRead

TEST_UUID1 = uuid4()
TEST_UUID2 = uuid4()
TEST_UUID3 = uuid4()
TEST_UUID4 = uuid4()

TEST_CATEGORY = TaskCategoryRead(
    public_id=TEST_UUID1,
    title="Sample Category",
    weight=40,
    priority=True,
    dailylimit=1000,
    totallimit=1000,
    enabled=True,
    colour="#FF0000",
    tasktype=1)
EXPECTED_SELECTABLE_TASK_FROM_CATEGORY = SelectableTask(
    public_id=TEST_UUID1,
    tasktype=1,
    title="Sample Category",
    parentcategoryname=None,
    dailylimit=1000,
    totallimit=1000,
    ratioweight=40,
    prioritypending=True,
    category_colour="#FF0000")


TEST_SUBTASK = SubTasksRead(
    public_id=TEST_UUID2,
    title="Sample Subtask1",
    weight=10,
    priority=False,
    dailylimit=1000,
    totallimit=1000,
    enabled=True,
    tasktype=2
    )

EXPECTED_SELECTABLE_TASK_FROM_SUBTASK = SelectableTask(
    public_id=TEST_UUID2,
    tasktype=2,
    title="Sample Subtask1",
    parentcategoryname=None,
    dailylimit=1000,
    totallimit=1000,
    ratioweight=10,
    prioritypending=False,
    category_colour="#808080")

TEST_SUBTASK2 = SubTasksRead(
    public_id=TEST_UUID3,
    title="Sample Subtask2",
    weight=25,
    priority=True,
    dailylimit=1,
    totallimit=1000,
    enabled=True,
    tasktype=2)
EXPECTED_SELECTABLE_TASK_FROM_SUBTASK2 = SelectableTask(
    public_id=TEST_UUID3,
    tasktype=2,
    title="Sample Subtask2",
    parentcategoryname=None,
    dailylimit=1,
    totallimit=1000,
    ratioweight=25,
    prioritypending=True,
    category_colour="#808080")



SAMPLE_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_EQUAL_WEIGHT = CategorySubtaskListRead(
        taskcategory=TaskCategoryRead(
            public_id=TEST_UUID1,
            title="Sample Category",
            weight=40,
            priority=True,
            dailylimit=1000,
            totallimit=1000,
            enabled=True,
            colour="#FF0000",
            tasktype=1),
        subtasks=[SubTasksRead(
            public_id=TEST_UUID2,
            title="Sample Subtask1",
            weight=25,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True,
            tasktype=2),
                SubTasksRead(
            public_id=TEST_UUID3,
            title="Sample Subtask2",
            weight=25,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True,
            tasktype=2)
        ])

EXPECTED_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_EQUAL_WEIGHT = [SelectableTask(
    public_id=TEST_UUID2,
    tasktype=2,
    title="Sample Subtask1",
    parentcategoryname="Sample Category",
    dailylimit=1000,
    totallimit=1000,
    ratioweight=20,
    prioritypending=False,
    category_colour="#FF0000"
    ), 
    SelectableTask(
    public_id=TEST_UUID3,
    tasktype=2,
    title="Sample Subtask2",
    parentcategoryname="Sample Category",
    dailylimit=1000,
    totallimit=1000,
    ratioweight=20,
    prioritypending=False,
    category_colour="#FF0000"
        )]

SAMPLE_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_UNEQUAL_WEIGHT_2 = CategorySubtaskListRead(
        taskcategory=TaskCategoryRead(
            public_id=TEST_UUID1,
            title="Sample Category",
            weight=40,
            priority=True,
            dailylimit=1000,
            totallimit=1000,
            enabled=True,
            colour="#FF0000",
            tasktype=1),
        subtasks=[SubTasksRead(
            public_id=TEST_UUID2,
            title="Sample Subtask1",
            weight=1,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True,
            tasktype=2),
        SubTasksRead(
            public_id=TEST_UUID3,
            title="Sample Subtask2",
            weight=3,
            priority=True,
            dailylimit=1,
            totallimit=1000,
            enabled=True,
            tasktype=2)
        ])



EXPECTED_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_UNEQUAL_WEIGHT_2 = [SelectableTask(
    public_id=TEST_UUID2,
    tasktype=2,
    title="Sample Subtask1",
    parentcategoryname="Sample Category",
    dailylimit=1000,
    totallimit=1000,
    ratioweight=10,
    prioritypending=False,
    category_colour="#FF0000"
    ), 
    SelectableTask(
    public_id=TEST_UUID3,
    tasktype=2,
    title="Sample Subtask2",
    parentcategoryname="Sample Category",
    ratioweight=30,
    dailylimit=1,
    totallimit=1000,
    prioritypending=True,
    category_colour="#FF0000")]

    

SAMPLE_CATEGORY_SUBTASK_LIST_THREE_SUBTASKS_UNEQUAL_WEIGHT = CategorySubtaskListRead(
        taskcategory=TaskCategoryRead(
            public_id=TEST_UUID1,
            title="Sample Category",
            weight=40,
            priority=True,
            dailylimit=1000,
            totallimit=1000,
            enabled=True,
            colour="#FF0000",
            tasktype=1),
        subtasks=[SubTasksRead(
            public_id=TEST_UUID2,
            title="Sample Subtask1",
            weight=5,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True),
        SubTasksRead(
            public_id=TEST_UUID3,
            title="Sample Subtask2",
            weight=5,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True),
        SubTasksRead(
            public_id=TEST_UUID4,
            title="Sample Subtask3",
            weight=10,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True)
        ])

EXPECTED_CATEGORY_SUBTASK_LIST_THREE_SUBTASKS_UNEQUAL_WEIGHT = [SelectableTask(
    public_id=TEST_UUID2,
    tasktype=2,
    title="Sample Subtask1",
    ratioweight=10,
    parentcategoryname="Sample Category",
    dailylimit=1000,
    totallimit=1000,
    prioritypending=False,
    category_colour="#FF0000"),
    SelectableTask(
    public_id=TEST_UUID3,
    tasktype=2,
    title="Sample Subtask2",
    ratioweight=10,
    parentcategoryname="Sample Category",
    prioritypending=False,
    dailylimit=1000,
    totallimit=1000,
    category_colour="#FF0000"),
        SelectableTask(
        public_id=TEST_UUID4,
        tasktype=2,
    title="Sample Subtask3",
    ratioweight=20,
    parentcategoryname="Sample Category",
    prioritypending=False,
    dailylimit=1000,
    totallimit=1000,
    category_colour="#FF0000")
]

SAMPLE_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_UNEQUAL_WEIGHT = CategorySubtaskListRead(
        taskcategory=TaskCategoryRead(
            public_id=TEST_UUID1,
            title="Sample Category",
            weight=40,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True,
            colour="#FF0000",
            tasktype=1),
        subtasks=[SubTasksRead(
            public_id=TEST_UUID2,
            title="Sample Subtask1",
            weight=25,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True),
        SubTasksRead(
            public_id=TEST_UUID3,
            title="Sample Subtask2",
            weight=75,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True)
        ])

EXPECTED_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_UNEQUAL_WEIGHT = [SelectableTask(
    public_id=TEST_UUID2,
    tasktype=2,
    title="Sample Subtask1",
    ratioweight=10,
    parentcategoryname="Sample Category",
    prioritypending=False,
    dailylimit=1000,
    totallimit=1000,
    category_colour="#FF0000"),
    SelectableTask(
    public_id=TEST_UUID3,
    tasktype=2,
    title="Sample Subtask2",
    ratioweight=30,
    parentcategoryname="Sample Category",
    prioritypending=True,
    dailylimit=1000,
    totallimit=1000,
    category_colour="#FF0000")]


SAMPLE_CATEGORY_SUBTASK_LIST_ONE_SUBTASK = CategorySubtaskListRead(
        taskcategory=TaskCategoryRead(
            public_id=TEST_UUID1,
            title="Sample Category",
            weight=40,
            priority=True,
            dailylimit=1000,
            totallimit=1000,
            enabled=True,
            colour="#FF0000",
            tasktype=1),
        subtasks=[SubTasksRead(
            public_id=TEST_UUID2,
            title="Sample Subtask1",
            weight=100,
            priority=False,
            dailylimit=1000,
            totallimit=1000,
            enabled=True)
        ])

EXPECTED_CATEGORY_SUBTASK_LIST_ONE_SUBTASK = [SelectableTask(
    public_id=TEST_UUID2,
    tasktype=2,
    title="Sample Subtask1",
    ratioweight=40,
    parentcategoryname="Sample Category",
    prioritypending=False,
    dailylimit=1000,
    totallimit=1000,
    category_colour="#FF0000")]
        

SAMPLE_CATEGORY_SUBTASK_LIST_NO_SUBTASKS = CategorySubtaskListRead(
        taskcategory=TaskCategoryRead(
            public_id=TEST_UUID1,
            title="Sample Category_no_subtasks",
            weight=40,
            priority=True,
            dailylimit=1000,
            totallimit=1000,
            enabled=True,
            colour="#FF0000",
            tasktype=1),
        subtasks=[])

EXPECTED_CATEGORY_SUBTASK_LIST_NO_SUBTASKS = [SelectableTask(
    public_id=TEST_UUID1,
    tasktype=1,
    title="Sample Category_no_subtasks",
    ratioweight=40,
    parentcategoryname=None,
    prioritypending=True,
    dailylimit=1000,
    totallimit=1000,
    category_colour="#FF0000")]

SAMPLE_USER_TASK_LIST_FULL_READ = UserTaskListFullRead(
        tasklist=[SAMPLE_CATEGORY_SUBTASK_LIST_NO_SUBTASKS, SAMPLE_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_EQUAL_WEIGHT])

EXPECTED_USER_TASK_LIST_FULL_READ = [SelectableTask(
    public_id=TEST_UUID1,
    tasktype=1,
    title="Sample Category_no_subtasks",
    ratioweight=40,
    parentcategoryname=None,
    prioritypending=True,
    dailylimit=1000,
    totallimit=1000,
    category_colour="#FF0000"),
    SelectableTask(
    public_id=TEST_UUID2,
    tasktype=2,
    title="Sample Subtask1",
    ratioweight=20,
    parentcategoryname="Sample Category",
    prioritypending=False,
    dailylimit=1000,
    totallimit=1000,
    category_colour="#FF0000",
    ),
    SelectableTask(
    public_id=TEST_UUID3,
    tasktype=2,
    title="Sample Subtask2",
    ratioweight=20,
    parentcategoryname="Sample Category",
    prioritypending=False,
    dailylimit=1000,
    totallimit=1000,
    category_colour="#FF0000"
    )    
]

SAMPLE_TASKLIST_FULL_READ_2 = UserTaskListFullRead(
    tasklist=[SAMPLE_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_EQUAL_WEIGHT, SAMPLE_CATEGORY_SUBTASK_LIST_THREE_SUBTASKS_UNEQUAL_WEIGHT])

EXPECTED_TASKLIST_FULL_READ_2 = EXPECTED_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_EQUAL_WEIGHT + EXPECTED_CATEGORY_SUBTASK_LIST_THREE_SUBTASKS_UNEQUAL_WEIGHT



"""
TASKLIST_FULL_READ_NO_SUBTASKS = UserTaskListFullRead(
    tasklist=[sample_category_subtask_list_no_subtasks])

TASKLIST_FULL_READ_TWO_SUBTASKS_EQUAL_WEIGHT = UserTaskListFullRead(
    tasklist=[sample_category_subtask_list_two_subtasks_equal_weight])

TASKLIST_FULL_READ_NO_SUBTASKS = UserTaskListFullRead(
    tasklist=[sample_category_subtask_list_no_subtasks])

"""


def test_convert_category_to_selectabletask():
    assert convert_category_to_selectabletask(TEST_CATEGORY) == EXPECTED_SELECTABLE_TASK_FROM_CATEGORY


def test_convert_subtask_to_selectabletask():
    assert convert_subtask_to_selectabletask(TEST_SUBTASK) == EXPECTED_SELECTABLE_TASK_FROM_SUBTASK
    assert convert_subtask_to_selectabletask(TEST_SUBTASK2) == EXPECTED_SELECTABLE_TASK_FROM_SUBTASK2



def test_calculate_subtask_weight():
    assert calculate_subtask_weight(10, 10, 25) == 25  
    assert calculate_subtask_weight(10, 20, 10) == 5
    assert calculate_subtask_weight(25, 100, 40) == 10
    assert calculate_subtask_weight(25, 75, 100) == 33.33

def test_calculate_category_tasks():
    assert calculate_category_tasks(SAMPLE_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_EQUAL_WEIGHT) == EXPECTED_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_EQUAL_WEIGHT
    assert calculate_category_tasks(SAMPLE_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_UNEQUAL_WEIGHT_2) == EXPECTED_CATEGORY_SUBTASK_LIST_TWO_SUBTASKS_UNEQUAL_WEIGHT_2
    assert calculate_category_tasks(SAMPLE_CATEGORY_SUBTASK_LIST_THREE_SUBTASKS_UNEQUAL_WEIGHT) == EXPECTED_CATEGORY_SUBTASK_LIST_THREE_SUBTASKS_UNEQUAL_WEIGHT
    assert calculate_category_tasks(SAMPLE_CATEGORY_SUBTASK_LIST_ONE_SUBTASK) == EXPECTED_CATEGORY_SUBTASK_LIST_ONE_SUBTASK
    assert calculate_category_tasks(SAMPLE_CATEGORY_SUBTASK_LIST_NO_SUBTASKS) == EXPECTED_CATEGORY_SUBTASK_LIST_NO_SUBTASKS


def test_calculate_user_task_list():
    assert calculate_user_task_list(SAMPLE_USER_TASK_LIST_FULL_READ) == EXPECTED_USER_TASK_LIST_FULL_READ
    assert calculate_user_task_list(SAMPLE_TASKLIST_FULL_READ_2) == EXPECTED_TASKLIST_FULL_READ_2
"""

"""