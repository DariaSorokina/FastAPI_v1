"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Acter

from .schemas import ActerCreate, ActerUpdate, ActerUpdatePartial


async def get_acters(session: AsyncSession) -> list[Acter]:
    stmt = select(Acter).order_by(Acter.id)
    result: Result = await session.execute(stmt)
    acters = result.scalars().all()
    return list(acters)


async def get_acter(session: AsyncSession, acter_id: int) -> Acter:
    return await session.get(Acter, acter_id)



async def create_acter(session: AsyncSession, acters_in: ActerCreate) -> Acter:
    acter = Acter(**acters_in.model_dump())
    session.add(acter)
    session.new
    await session.commit()
    await session.refresh(acter)
    return acter


async def update_acter(
    session: AsyncSession,
    acter: Acter,
    acter_update: ActerUpdate,
    partial: bool = False,
) -> Acter:
    for name, value in acter_update.model_dump(exclude_unset=partial).items():
        setattr(acter, name, value)
    await session.commit()
    return acter


async def delete_acter(
    session: AsyncSession,
    acter: Acter,
) -> None:
    await session.delete(acter)
    await session.commit()