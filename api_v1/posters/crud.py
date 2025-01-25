"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Poster

from .schemas import PosterCreate, PosterUpdate, PosterUpdatePartial


async def get_posters(session: AsyncSession) -> list[Poster]:
    stmt = select(Poster).order_by(Poster.id)
    result: Result = await session.execute(stmt)
    posters = result.scalars().all()
    return list(posters)


async def get_poster(session: AsyncSession, poster_id: int) -> Poster:
    return await session.get(Poster, poster_id)


async def create_poster(session: AsyncSession, poster_in: PosterCreate) -> Poster:
    poster = Poster(**poster_in.model_dump())
    session.add(poster)
    session.new
    await session.commit()
    await session.refresh(poster)
    return poster


async def update_poster(
    session: AsyncSession,
    poster: Poster,
    poster_update: PosterUpdate, #ProductUpdatePartial
    partial: bool = False,
) -> Poster:
    for name, value in poster_update.model_dump(exclude_unset=partial).items():
        setattr(poster, name, value)
    await session.commit()
    return poster


async def delete_poster(
    session: AsyncSession,
    poster: Poster,
) -> None:
    await session.delete(poster)
    await session.commit()