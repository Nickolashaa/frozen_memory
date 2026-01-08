from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..cronjobs.note_reminder import note_remind
from ..utils.is_admin import is_admin


manual_cron_router = Router()


@manual_cron_router.message(Command("activate_cron"))
async def manual_activate_cron(message: Message):
    if is_admin(message.from_user.id):
        await message.answer("START")
        await note_remind(bot=message.bot)
        await message.answer("STOP")
    else:
        await message.answer("Доступ запрещен!")
