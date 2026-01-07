from aiogram import Router

from .auth import auth_router
from .manual_cron import manual_cron_router
from .note import note_router


def get_routers() -> Router:
    router = Router()

    router.include_router(auth_router)
    router.include_router(manual_cron_router)
    router.include_router(note_router)

    return router
