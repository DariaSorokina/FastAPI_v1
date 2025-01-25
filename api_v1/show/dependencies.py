from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Show

from . import crud


async def show_by_id(
    show_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Show:
    show = await crud.get_show(session=session, show_id=show_id)
    if show is not None:
        return show

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Show {show_id} not found!",
    )