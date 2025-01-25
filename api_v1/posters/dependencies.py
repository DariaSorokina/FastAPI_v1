from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Poster

from . import crud


async def poster_by_id(
    poster_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Poster:
    poster = await crud.get_poster(session=session, poster_id=poster_id)
    if poster is not None:
        return poster

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Poster {poster_id} not found!",
    )