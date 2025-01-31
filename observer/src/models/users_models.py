from tortoise import Model, fields

from models.tasks_models import Task


class User(Model):
    user_id = fields.IntField()

    tasks: fields.ForeignKeyRelation[Task]
