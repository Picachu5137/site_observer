from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


user_commands: dict[str, str] = {
    "help": "Вывод помощи",
    "add_task": "Добавление нового наблюдателя",
    "list_tasks": "Список активных наблюдателей",
}

async def set_default_commands(bot: Bot) -> None:
    await remove_default_commands(bot)

    await bot.set_my_commands(
        commands=[BotCommand(command=command, description=description) for command, description in user_commands.items()],
        scope=BotCommandScopeDefault()
    )

async def remove_default_commands(bot: Bot) -> None:
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    