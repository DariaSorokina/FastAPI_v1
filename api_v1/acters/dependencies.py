from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Acter

from . import crud


async def acter_by_id(
    acter_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Acter:
    acter = await crud.get_acter(session=session, acter_id=acter_id)
    if acter is not None:
        return acter

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Acter {acter_id} not found!",
    )