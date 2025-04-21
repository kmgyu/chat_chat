from celery import shared_task
import logging
logger = logging.getLogger(__name__)

@shared_task
def print_hello():
    logger.info(">>> 주기적으로 실행 중! Hello from Celery via logger!")

# celery tasks

# @shared_task
# def print_hello():
#     print(">>> 주기적으로 실행 중! Hello from Celery!")
