from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter

class AddTaskState(StatesGroup):
    menu = State()
    name =State()
    url = State()
    xpath = State()
    time_period = State()
    