from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Ticket

from . import crud


async def ticket_by_id(
    ticket_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Ticket:
    ticket = await crud.get_ticket(session=session, ticket_id=ticket_id)
    if ticket is not None:
        return ticket

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Ticket {ticket_id} not found!",
    )