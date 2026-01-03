from aiogram import Bot, Dispatcher

from config import settings

from .handlers import get_routers


async def main():
    bot = Bot(token=settings.TG_TOKEN)
    dp = Dispatcher()

    dp.include_router(get_routers())

    print("Bot start work...")
    await dp.start_polling(bot)
