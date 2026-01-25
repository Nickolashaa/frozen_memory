from aiogram import Bot

from config import settings
from .data_compiler import compile
from .post_generator import PostGenerator
from ...database import async_session_maker
from ...services.notes.types import TimeInterval


async def generate_posts(
    interval: TimeInterval,
    bot: Bot,
) -> None:
    report: dict[str, bool] = {}
    str_report = str()
    success_count = 0

    async with async_session_maker() as session:
        compiled_data_list = await compile(session=session, interval=interval)

        for data in compiled_data_list:
            try:
                post = await PostGenerator.generate_post(data)
                await bot.send_message(
                    chat_id=data.user_id, text=post, parse_mode="HTML"
                )
                report[data.user_name] = True
                success_count += 1
            except Exception as e:
                await bot.send_message(
                    chat_id=settings.ADMIN,
                    text=f"Ошибка генерации поста для пользователя {data.user_name}: {e}",
                )
                report[data.user_name] = False
                continue

    for key, value in report.items():
        str_report += f"{key}: {value}\n"
    str_report += f"Итого: {success_count}/{len(report.keys())}"
    await bot.send_message(
        chat_id=settings.ADMIN,
        text=str_report,
    )
