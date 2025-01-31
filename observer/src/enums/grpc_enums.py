from enum import Enum


class CheckPeriod("str", Enum):
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"


class CheckMethod("str", Enum):
    TEXT = "TEXT"
    HTML = "HTML"
    