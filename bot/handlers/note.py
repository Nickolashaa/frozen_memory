from aiogram import Router
from aiogram.types import Message, ReactionTypeEmoji

from ..database import async_session_maker
from ..services.notes import NoteService


note_router = Router()


@note_router.message()
async def create_note(message: Message):
    async with async_session_maker() as session:
        await NoteService.create(
            session=session,
            user_id=message.from_user.id,
            text=message.text,
        )
        await session.commit()

    await message.react([ReactionTypeEmoji(emoji="❤️")])
