from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Unpack

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from .types import NoteParams, TimeInterval
from ...models.notes import Note
from ...schemas import NoteDTO


class NoteService:
    @staticmethod
    async def create(session: AsyncSession, **values: Unpack[NoteParams]) -> NoteDTO:
        stmt = insert(Note).values(**values).returning(Note)

        res = await session.execute(stmt)
        instance = res.scalar_one()

        return NoteDTO.model_validate(obj=instance, from_attributes=True)

    @staticmethod
    async def get_list(
        session: AsyncSession,
        user_id: int,
        interval: TimeInterval,
    ) -> list[NoteDTO]:
        stmt = select(Note).where(Note.user_id == user_id)

        match interval:
            case "ALL_TIME":
                pass
            case "MONTH":
                one_month_ago = datetime.now() - relativedelta(months=1)
                stmt = stmt.where(Note.created_at >= one_month_ago)
            case "YEAR":
                one_year_ago = datetime.now() - relativedelta(years=1)
                stmt = stmt.where(Note.created_at >= one_year_ago)

        res = await session.execute(stmt)

        return [
            NoteDTO.model_validate(obj=instance, from_attributes=True)
            for instance in res.scalars()
        ]
