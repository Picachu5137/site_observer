from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from loguru import logger

from states.observer_states import AddTaskState
from keyboards.inline.menu import add_task_keyboard
from templates.template_engine import render_template


observer_router = Router(name="observer_router")


@observer_router.message(Command("add_task"), StateFilter(None))
async def add_task(message: types.Message, state: FSMContext):
    await state.set_state(AddTaskState.menu)
    await state.update_data(
        {
        "name": "",
        "url": "",
        "xpath": "",
        "check_method": "HTML",
        "check_period": "DAILY",
        }
    )
    data = await state.get_data()
    logger.debug(f"{data=}")

    await message.answer(
        render_template("add_task_menu.html", **data), 
        reply_markup=add_task_keyboard()
    )

@observer_router.callback_query(lambda c: c.data == "menu")
async def add_task_menu(callback: types.CallbackQuery, state: FSMContext):

    return await callback.message.answer(render_template("add_task_menu.html", **callback.data), reply_markup=add_task_keyboard())


@observer_router.callback_query(lambda c: c.data == "set_name")
async def set_task_name(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(AddTaskState.name)
    await callback.message.edit_text(render_template("add_task_name.html"))
