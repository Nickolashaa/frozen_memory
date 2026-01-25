from sqlalchemy.ext.asyncio import AsyncSession

from ...schemas import CompiledData
from ...services.notes import NoteService
from ...services.notes.types import TimeInterval
from ...services.users import UserService


async def compile(session: AsyncSession, interval: TimeInterval) -> list[CompiledData]:
    result: list[CompiledData] = []

    users = await UserService.get_all(session=session)

    for user in users:
        notes = await NoteService.get_list(
            session=session,
            user_id=user.id,
            interval=interval,
        )
        result.append(
            CompiledData(
                user_id=user.id,
                user_name=user.first_name,
                notes=[note.text for note in notes],
            )
        )

    return result
