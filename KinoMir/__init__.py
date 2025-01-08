from typing import Tuple

from dotenv import load_dotenv

from .celery import app as celery_app

load_dotenv()

__all__: Tuple = ("celery_app",)
