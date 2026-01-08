from aiogram import Router

from .auth import auth_router
from .manual_cron import manual_cron_router
from .note import note_router
from .text_dispatch import text_dispatch_router


def get_routers() -> Router:
    router = Router()

    # Авторизация
    router.include_router(auth_router)

    # Команды
    router.include_router(manual_cron_router)
    router.include_router(text_dispatch_router)

    # Записи
    router.include_router(note_router)

    return router
