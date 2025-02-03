from tortoise import Model, fields

from models.mixins import BaseModel
from models.users_models import User
from enums.grpc_enums import CheckPeriod, CheckMethod


class Task(BaseModel):
    user_id = fields.ForeignKeyField(
        model_name="User",
        related_name="tasks",
        on_delete=fields.CASCADE
    )

    name = fields.CharField(max_length=128)

    last_check = fields.DatetimeField(auto_now=True)

    check_period = fields.CharEnumField(CheckPeriod)
    check_method = fields.CharEnumField(CheckMethod)

    url = fields.CharField(max_length=100)

    xpath = fields.CharField(max_length=255)

    element_hash = fields.CharField(max_length=64)
