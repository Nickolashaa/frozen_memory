from asyncio import sleep

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from ..database import async_session_maker
from ..services.users import UserService


auth_router = Router()


@auth_router.message(CommandStart())
async def start(message: Message):
    async with async_session_maker() as session:
        await UserService.create(
            session=session,
            id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
        await session.commit()
    await message.answer("Привет! Я помогу тебе запомнить весь 2026 год!")
    await sleep(1)
    await message.answer(
        "Просто пиши мне о том, как прошел твой день, я буду запоминать, а в конце каждого месяца и под Новый Год буду присылать тебе пост 'Мои итоги месяца/года'"
    )
