from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from bot.states.observer_states import AddTaskState


observer_router = Router(name="observer_router")


@observer_router.message(Command("add_task"), StateFilter(None))
async def add_task(message: types.Message, state: FSMContext):
    await state.set_state(AddTaskState.menu)
    await state.update_data(task={
        "name": "",
        "url": "",
        "xpath": "",
    })
    return await message.answer("Введите название ")


@observer_router.callback_query(lambda c: c.data == "set_name")
async def set_task_name(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit("Введите ")
