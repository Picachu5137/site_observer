from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def add_task_keyboard() -> InlineKeyboardMarkup:
    """
    Use in add_task menu
    """
    buttons = [
        [InlineKeyboardButton(text="Изменить название", callback_data="set_name")],
        [InlineKeyboardButton(text="Изменить URL", callback_data="set_url")],
        [InlineKeyboardButton(text="Изменить XPath", callback_data="set_xpath")],
        [InlineKeyboardButton(text="Изменить частоту проверки", callback_data="set_check_period")],
        [InlineKeyboardButton(text="Создать", callback_data="create")],
        [InlineKeyboardButton(text="Отмена", callback_data="cancel")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    keyboard.adjust(1, 1, 1, 1, 2)

    return keyboard.as_markup()

def single() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    return keyboard.as_markup()
