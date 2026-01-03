from typing import Unpack

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from .types import UserParams
from ...models.users import User
from ...schemas import UserDTO


class UserService:
    @staticmethod
    async def create(
        session: AsyncSession,
        **values: Unpack[UserParams],
    ) -> UserDTO | None:
        id = values.get("id")
        if id is None:
            return

        select_stmt = select(User).where(User.id == id)

        select_res = await session.execute(select_stmt)
        instance = select_res.scalar_one_or_none()
        if instance is not None:
            return

        insert_stmt = insert(User).values(**values).returning(User)

        res = await session.execute(insert_stmt)
        instance = res.scalar_one()

        return UserDTO.model_validate(obj=instance, from_attributes=True)
