from tortoise import Model, fields

from models.mixins import BaseModel
from models.tasks_models import Task


class User(BaseModel):
    user_id = fields.IntField()
    tasks: fields.ForeignKeyRelation[Task]
