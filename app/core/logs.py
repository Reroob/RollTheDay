import logging
from app.core.config import settings
import sys

LOG_FORMAT="%(asctime)s [%(levelname)s] %(name)s: %(message)s"

logging.basicConfig(
    level=settings.log_level,
    format=LOG_FORMAT,
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger('mileageapp')

