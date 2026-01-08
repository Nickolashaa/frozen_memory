from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from ..database import async_session_maker
from ..services.users import UserService
from ..utils.is_admin import is_admin


text_dispatch_router = Router()


@text_dispatch_router.message(Command("dispatch"))
async def create_text_dispatch(message: Message):
    if is_admin(message.from_user.id):
        text = message.text.replace("/dispatch", "")

        async with async_session_maker() as session:
            users = await UserService.get_all(
                session=session,
            )

        report = dict()
        str_report = str()
        success_count = 0

        for user in users:
            try:
                await message.bot.send_message(
                    chat_id=user.id,
                    text=text,
                )
                report[user.id] = True
                success_count += 1
            except Exception:
                report[user.id] = False

        for key, value in report.items():
            str_report += f"{key}: {value}\n"
        str_report += f"Итого: {success_count}/{len(report.keys())}"

        await message.answer(str_report)
    else:
        await message.answer("Доступ запрещен!")
