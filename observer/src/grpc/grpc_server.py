from main import app

from schemas.grpc_schemas import AddTaskRequest, DeleteTaskRequest, UpdateTaskRequest, Empty
from models.tasks_models import Task


@app.unary_unary()
async def add_task(request: AddTaskRequest) -> Empty:
    task = await Task.create(
        user_id=request.user_id,
        check_period=request.check_period,
        url=request.url,
        xpath=request.xpath,
    )
    