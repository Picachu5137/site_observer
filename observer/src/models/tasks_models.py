from tortoise import Model, fields

from models.users_models import User
from enums.grpc_enums import CheckPeriod, CheckMethod


class Task(Model):
    user_id = fields.ForeignKeyField(
        model_name="User",
        related_name="tasks",
        on_delete=fields.CASCADE
    )

    last_check = fields.DatetimeField(auto_now=True)

    check_period = fields.CharEnumField(CheckPeriod)
    check_method = fields.CharEnumField(CheckMethod)

    url = fields.CharField(max_length=100)

    xpath = fields.CharField(max_length=255)

    element_hash = fields.CharField(max_length=64)
