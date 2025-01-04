from typing import Tuple
from .celery import app as celery_app

from dotenv import load_dotenv

load_dotenv()

__all__: Tuple = ('celery_app',)
