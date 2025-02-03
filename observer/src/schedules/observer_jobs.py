from models.tasks_models import Task
from observer.observer import PageObserver


async def check_sites():
    tasks = await Task.all()

    for task in tasks:
        observer = PageObserver(task)
        await observer.detect_page_changes()
