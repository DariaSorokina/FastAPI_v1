"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Show

from .schemas import ShowCreate, ShowUpdate


async def get_shows(session: AsyncSession) -> list[Show]:
    stmt = select(Show).order_by(Show.id)
    result: Result = await session.execute(stmt)
    shows = result.scalars().all()
    return list(shows)


async def get_show(session: AsyncSession, show_id: int) -> Show:
    return await session.get(Show, show_id)


async def create_show(session: AsyncSession, show_in: ShowCreate) -> Show:
    show = Show(**show_in.model_dump())
    session.add(show)
    session.new
    await session.commit()
    return show


async def update_show(
    session: AsyncSession,
    show: Show,
    show_update: ShowUpdate,
    partial: bool = False,
) -> Show:
    for name, value in show_update.model_dump(exclude_unset=partial).items():
        setattr(show, name, value)
    await session.commit()
    return show


async def delete_show(
    session: AsyncSession,
    show: Show,
) -> None:
    await session.delete(show)
    await session.commit()