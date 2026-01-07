from aiogram import Bot, Dispatcher

from config import settings

from .handlers import get_routers
from .cronjobs import setup_sheduler


async def main():
    bot = Bot(token=settings.TG_TOKEN)
    dp = Dispatcher()

    dp.include_router(get_routers())

    scheduler = setup_sheduler(bot=bot)
    scheduler.start()

    print("Bot start work...")
    await dp.start_polling(bot)
