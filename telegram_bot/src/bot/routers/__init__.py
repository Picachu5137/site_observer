from aiogram import Router

from bot.routers.observer_routes import observer_router


main_router = Router()

main_router.include_router(observer_router)


