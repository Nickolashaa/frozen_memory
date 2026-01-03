from typing import Unpack

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from .types import NoteParams
from ...models.notes import Note
from ...schemas import NoteDTO


class NoteService:
    @staticmethod
    async def create(session: AsyncSession, **values: Unpack[NoteParams]) -> NoteDTO:
        stmt = insert(Note).values(**values).returning(Note)

        res = await session.execute(stmt)
        instance = res.scalar_one()

        return NoteDTO.model_validate(obj=instance, from_attributes=True)
