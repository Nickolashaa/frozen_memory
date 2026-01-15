import asyncio

from aiogram import Router, F
from aiogram.types import Message, ReactionTypeEmoji

from ..database import async_session_maker
from ..services.notes import NoteService
from ..services.voice_to_text import VoiceToTextService


note_router = Router()


@note_router.message(F.text)
async def create_note(message: Message):
    async with async_session_maker() as session:
        await NoteService.create(
            session=session,
            user_id=message.from_user.id,
            text=message.text,
        )
        await session.commit()

    await message.react([ReactionTypeEmoji(emoji="❤️")])


@note_router.message(F.voice)
async def create_voice_note(message: Message):
    await message.react([ReactionTypeEmoji(emoji="👀")])

    try:
        file = await message.bot.get_file(message.voice.file_id)
        audio_file = await message.bot.download_file(file.file_path)
        audio_bytes = audio_file.read()

        text = await asyncio.to_thread(
            VoiceToTextService.bytes_to_text,
            audio_bytes,
            "ru",
        )

        async with async_session_maker() as session:
            await NoteService.create(
                session=session,
                user_id=message.from_user.id,
                text=text,
            )
            await session.commit()

        await message.react([ReactionTypeEmoji(emoji="❤️")])
    except Exception:
        await message.react([ReactionTypeEmoji(emoji="❌")])
