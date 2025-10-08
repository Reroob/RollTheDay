from app.tasks import crud
from app.tasks import schemas
from app.tasks.schemas import UserTaskListFullRead
from sqlmodel import Session
from app.core.db import get_session     
import random
import logging
logger = logging.getLogger(__name__)

colourlist = {
    'Coral Red': '#E63946',
    'Warm Orange': '#F3722C',
    'Golden Yellow': '#F9C74F',
    'Fresh Green': '#90BE6D',
    'Teal Green': '#43AA8B',
    'Muted Blue': '#577590',
    'Deep Sky Blue': '#277DA1',
    'Seafoam': '#4D908E',
    'Tangerine': '#F9844A',
    'Plum': '#A05195',
    'Vivid Purple': '#8338EC',
    'Electric Blue': '#3A86FF',
    'Magenta Pink': '#FF006E',
    'Orange Red': '#FB5607',
    'Mocha Brown': '#9C6644',
    'Cool Gray': '#6C757D'
}


def get_user_full_tasks(userid: int, session: Session) -> schemas.UserTaskListFullRead:
    completetasklist = []
    categorylist= crud.get_categories_by_userid(session, userid)
    for category in categorylist:
        completetasklist.append(crud.get_category_and_subtasks_by_category_publicid(session, category.public_id))
    return schemas.UserTaskListFullRead(tasklist=completetasklist)

def set_category_colours():
    return

def calculate_category_ratios(categorylist: list[schemas.TaskCategoryRead]) -> list[schemas.CategoryPercentageRead]:
    # calculate the percentage of each category
    total_weight = sum(category.weight for category in categorylist)
    logger.info(f'Total weight: {total_weight}')
    category_percentages = []
    for category in categorylist:
        title = category.title
        percentage = round (category.weight / total_weight * 100, 0)
        colour = category.colour
        category_percentages.append(schemas.CategoryPercentageRead(category=title, percentage=percentage, colour=colour))
    return category_percentages
 

