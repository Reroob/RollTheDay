from app.tasks import crud
from app.tasks import schemas
from sqlmodel import Session
from app.tasks.routes import get_category_and_subtasks_by_category_publicid
from app.core.db import get_session     

def get_user_full_tasks(userid: int) -> schemas.UserTaskListFullRead:
    session = next(get_session())
    completetasklist = []
    categorylist= crud.get_categories_by_userid(session, userid)
    for category in categorylist:
        completetasklist.append(get_category_and_subtasks_by_category_publicid(session, category.public_id))
    return schemas.UserTaskListFullRead(tasklist=completetasklist)