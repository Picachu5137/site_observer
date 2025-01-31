from enum import Enum
from typing import Optional

from pydantic import BaseModel, field_validator, HttpUrl, Field
from lxml.etree import XPath, XPathSyntaxError

from enums.grpc_enums import CheckPeriod, CheckMethod
from schemas.validators import validate_xpath


class AddTaskRequest(BaseModel):
    user_id: int
    name: str
    url: HttpUrl
    xpath: str
    check_period: CheckPeriod
    check_method: CheckMethod

    @field_validator("xpath")
    @classmethod
    def validate_xpath(cls, v: Any):
        validate_xpath(v)

class DeleteTaskRequest(BaseModel):
    user_id: int
    task_id: int = Field(ge=0)

class UpdateTaskRequest(BaseModel):
    user_id: int
    task_id: int
    name: Optional[str]
    url: Optional[HttpUrl]
    xpath: Optional[str]
    check_period: Optional[CheckPeriod]
    check_method: Optional[CheckMethod]

    @field_validator("xpath")
    @classmethod
    def validate_xpath(cls, v: Any):
        validate_xpath(v)

class Empty(BaseModel):
    pass