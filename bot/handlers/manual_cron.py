from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..cronjobs.note_reminder import note_remind


manual_cron_router = Router()


@manual_cron_router.message(Command("activate_cron"))
async def manual_activate_cron(message: Message):
    await message.answer("START")
    await note_remind(bot=message.bot)
    await message.answer("STOP")
