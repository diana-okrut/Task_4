from .celery import app
from celery.utils.log import get_task_logger
from celery import Task


class MyStaticTask(Task):
    name = 'MyStaticTask'

    def run(self, *args, **kwargs):
        print("Слава Україні! Жыве Беларусь!")


class MyPeriodicTask(Task):

    def run(self, *args, **kwargs):
        logger = get_task_logger(__name__)
        logger.info("The sample task just ran.")


app.register_task(MyStaticTask)
app.register_task(MyPeriodicTask)
